#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 Bing 图片搜索采集初学标注练习用的真实网络图片。

用法:
    python scripts/collect_web_images.py                 # 每类 20 张，全量采集
    python scripts/collect_web_images.py --per-class 5   # 少量试跑
    python scripts/collect_web_images.py --only phone    # 只采某一类

输出:
    data/raw/<类别>/NNN.jpg          图片本体（顺序编号）
    data/raw/manifest.csv            来源清单（URL/尺寸/哈希/授权页），写报告"数据集说明"用

设计说明:
    - 当前校园网下 Wikimedia / Openverse / DuckDuckGo 均不可达，只有 Bing 图片搜索的
      HTML 里能解析出原图直链(murl)，故走这条路。
    - 采集时"多下载"，靠质量门槛筛掉不合格的，而不是靠搜索精度。筛不掉的部分必须人工复查。
"""
import argparse
import csv
import hashlib
import io
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote, urlparse

import requests

try:
    from PIL import Image
except ImportError:
    Image = None

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}

# 每类用多个查询词轮换，提高多样性。
# 关键经验：中文"实拍/特写"类查询会命中新闻站、评测站、社区图床（新华网/什么值得买/知乎/
# 少数派等），水印率远低于英文通用词——英文通用词会被 dreamstime/alamy 这类带水印图库站
# 和 amazon/walmart 这类白底电商图霸占首屏。
QUERIES = {
    "phone":   ["手机 评测 图赏 桌面", "iPhone 真机 上手 桌面", "智能手机 评测 实拍 桌上", "安卓手机 图赏 桌面"],
    "bottle":  ["矿泉水瓶 晒单 实拍 桌面", "饮料瓶 评测 图赏 桌上", "塑料瓶 晒物 实拍", "纯净水瓶 实拍 桌面"],
    "charger": ["充电器 数据线 晒单 实拍", "充电头 评测 图赏 桌面", "数据线 晒物 实拍 桌上", "快充 充电器 评测 实拍"],
    "key":     ["钥匙串 晒单 实拍 桌面", "机械钥匙 特写 实拍", "一串钥匙 图赏 桌面", "车钥匙 晒物 实拍"],
    "cup":     ["杯子 晒单 实拍 桌上", "马克杯 评测 图赏 桌面", "陶瓷杯 晒物 实拍", "星巴克 马克杯 实拍 桌面"],
}

# 图库/素材水印站 + 电商白底图 + 二手交易平台，按域名剔除。
# 注意必须中英双语都覆盖：中文站(摄图网/昵图网/千图网等)在中文查询下的霸屏程度和英文站一样高。
BLOCK_HOSTS = (
    # 英文图库
    "dreamstime", "alamy", "shutterstock", "gettyimages", "istockphoto", "123rf",
    "depositphotos", "bigstockphoto", "bigstock", "photodune", "pond5", "feature-pics",
    "canva", "flaticon", "freepik", "ebs", "happynews", "agefotostock", "cutcaster",
    "robertsphoto", "mint", "icon8", "veer", "123rf",
    # 中文图库/素材站
    "699pic", "nipic", "redocn", "huitu", "58pic", "588ku", "tukuppt", "ibaotu",
    "sucai999", "qiantumeitu", "toomei", "meijie", "16pic", "w7cc", "52112",
    "zaixanjia", "pdfforg", "renrendoc", "mianfeiwendang", "51wendang", "doc88",
    "jiazhao", "baobei", "tuchong", "qiantucdn", "qiantu",
    # 电商白底商品图
    "media-amazon", "amazon", "walmart", "ebay", "ebayimg", "taobao", "tmall",
    "jd.com", "cbu01.alicdn", "alicdn", "aliexpress", "bestbuy", "etsy", "picclick",
    "c-and-a", "jcpenney", "macys", "nordstrom", "overstock", "wayfair", "kogan",
    "shopstyle", "stardust", "wikimedia", "qunarzz",
)

# 质量门槛：低于任一门槛直接丢弃
MIN_SHORT_SIDE = 360     # 短边像素，太小无法标注细节
MIN_LONG_SIDE = 520      # 长边像素
MAX_ASPECT = 2.5         # 长宽比，剔除横幅/条图/截图
MIN_BYTES = 15_000
MAX_BYTES = 8_000_000


def search_urls(query, pages=2):
    """从 Bing 图片搜索结果页解析原图直链。"""
    found = []
    for page in range(pages):
        params = {"q": query, "form": "HDRSC2", "first": 35 * page + 1,
                  "count": 35, "aspect": "square,wide", "qft": "+filterui:photo-photo"}
        try:
            r = requests.get("https://www.bing.com/images/search",
                             params=params, headers=HEADERS, timeout=20)
            r.raise_for_status()
        except Exception as e:
            print(f"    [warn] 搜索失败 '{query}' p{page}: {type(e).__name__}", file=sys.stderr)
            continue
        found += re.findall(r'murl&quot;:&quot;(https?://.+?)&quot;', r.text)
        time.sleep(0.6)
    seen, out = set(), []
    dropped = 0
    for u in found:
        u = u.replace("&amp;", "&")
        host = urlparse(u).netloc.lower()
        if any(b in host for b in BLOCK_HOSTS):
            dropped += 1
            continue
        if u not in seen:
            seen.add(u)
            out.append(u)
    if dropped:
        print(f"      (剔除图库/电商来源 {dropped} 个)")
    return out


def evaluate(content):
    """校验字节流是否为合格图片，返回 (w, h) 或 None。"""
    if not (MIN_BYTES <= len(content) <= MAX_BYTES):
        return None
    if content[:3] != b"\xff\xd8\xff" and content[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if Image is None:
        return (0, 0)
    try:
        with Image.open(io.BytesIO(content)) as im:
            im.verify()
            with Image.open(io.BytesIO(content)) as im2:
                w, h = im2.size
    except Exception:
        return None
    if min(w, h) < MIN_SHORT_SIDE or max(w, h) < MIN_LONG_SIDE:
        return None
    if max(w, h) / max(1, min(w, h)) > MAX_ASPECT:
        return None
    return (w, h)


def try_download(url, dest, manifest_row):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            return None
        wh = evaluate(r.content)
        if not wh:
            return None
        digest = hashlib.md5(r.content).hexdigest()
        if dest in manifest_row["_done"] or digest in manifest_row["_hashes"]:
            return None
        with open(dest, "wb") as f:
            f.write(r.content)
        manifest_row["_done"].add(dest)
        manifest_row["_hashes"].add(digest)
        return {"path": dest, "width": wh[0], "height": wh[1], "bytes": len(r.content),
                "md5": digest, "source_url": url,
                "license_note": "网络图片，版权归原作者，仅供本地标注练习；不可用于对外发布，"
                                "也不可写成自己采集的数据提交"}
    except Exception:
        return None


def collect(cls, queries, out_dir, per_class, state, append=False):
    target_dir = os.path.join(out_dir, cls)
    os.makedirs(target_dir, exist_ok=True)
    # 续编号模式：补采时不覆盖已有图片（否则 001.jpg 会被重写，manifest 与磁盘不一致）
    if append:
        existing = [f for f in os.listdir(target_dir) if f.lower().endswith(".jpg")]
        nums = [int(os.path.splitext(f)[0]) for f in existing if os.path.splitext(f)[0].isdigit()]
        got = max(nums) if nums else 0
        per_class = got + per_class
        print(f"[{cls}] 已有 {got} 张，续编号补采至 {per_class} 张")
    else:
        got = 0
        print(f"[{cls}] 目标 {per_class} 张")
    for qi, q in enumerate(queries):
        if got >= per_class:
            break
        urls = search_urls(q, pages=2)
        print(f"    查询 '{q}' → 候选 {len(urls)} 个")
        need = per_class - got
        batch = urls[: need * 6]          # 多下一倍，靠门槛筛
        with ThreadPoolExecutor(max_workers=8) as ex:
            futs = {}
            for i, u in enumerate(batch):
                dest = os.path.join(target_dir, f"{qi:02d}_{i:03d}.jpg")
                futs[ex.submit(try_download, u, dest, state)] = dest
            for fu in as_completed(futs):
                if got >= per_class:
                    continue
                rec = fu.result()
                if rec:
                    got += 1
                    final = os.path.join(target_dir, f"{got:03d}.jpg")
                    os.rename(rec["path"], final)
                    rec["path"] = final
                    rec["category"] = cls
                    rec["query"] = q
                    state["rows"].append(rec)
        # 清理未采用的临时文件
        for p in os.listdir(target_dir):
            if p.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")) and "_" in p:
                try:
                    os.remove(os.path.join(target_dir, p))
                except OSError:
                    pass
    print(f"[{cls}] 实际到手 {got} 张  →  {target_dir}")
    return got


def write_manifest(out_dir, new_rows, append):
    """manifest 永远反映磁盘现状：已有行按 path 保留，本次新图覆盖同名 path。"""
    mf = os.path.join(out_dir, "manifest.csv")
    cols = ["category", "path", "query", "width", "height", "bytes", "md5",
            "source_url", "license_note"]
    merged = {}
    if append and os.path.exists(mf):
        with open(mf, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if os.path.exists(r.get("path", "")):
                    merged[r["path"]] = r
    for r in new_rows:
        merged[r["path"]] = r
    rows = sorted(merged.values(), key=lambda r: (r["category"], r["path"]))
    with open(mf, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return len(rows), mf


def rebuild_manifest(out_dir):
    """只扫盘重建 manifest，不下载。用于修数据或补采后对齐清单。"""
    mf = os.path.join(out_dir, "manifest.csv")
    old = {}
    if os.path.exists(mf):
        with open(mf, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                old[os.path.basename(r.get("path", "")) + "|" + r.get("category", "")] = r
    rows, missing = [], 0
    for cls in sorted(os.listdir(out_dir)):
        d = os.path.join(out_dir, cls)
        if not os.path.isdir(d) or cls.startswith(("_", ".")) or cls == "review":
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            p = os.path.abspath(os.path.join(d, fn))
            prev = old.get(f"{fn}|{cls}")
            with open(p, "rb") as fh:
                content = fh.read()
            if prev and prev.get("md5") == hashlib.md5(content).hexdigest():
                r = dict(prev)
            else:  # 内容变了或没见过 → 来源不可考，如实标注
                missing += 1
                r = {"category": cls, "query": "-", "source_url": "-",
                     "license_note": "来源未能追溯（清单曾被覆盖），请人工核对后再使用"}
            wh = evaluate(content) or (0, 0)
            r.update({"path": p, "width": wh[0], "height": wh[1],
                      "bytes": len(content), "md5": hashlib.md5(content).hexdigest()})
            rows.append(r)
    cols = ["category", "path", "query", "width", "height", "bytes", "md5",
            "source_url", "license_note"]
    with open(mf, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["category"], r["path"])))
    print(f"manifest 重建: {len(rows)} 条，其中来源不可考 {missing} 条 → {mf}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-class", type=int, default=20)
    ap.add_argument("--only", nargs="*", default=list(QUERIES))
    ap.add_argument("--append", action="store_true",
                    help="续编号补采，不覆盖已有图片")
    ap.add_argument("--rebuild-manifest", action="store_true",
                    help="不下载，只按磁盘现状重建 manifest")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "data", "raw"))
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    if args.rebuild_manifest:
        rebuild_manifest(args.out)
        return

    state = {"rows": [], "_done": set(), "_hashes": set()}
    if args.append:  # 预载已有图哈希，避免补采下到重复内容
        for cls in args.only:
            d = os.path.join(args.out, cls)
            if not os.path.isdir(d):
                continue
            for f in os.listdir(d):
                p = os.path.join(d, f)
                if os.path.isfile(p):
                    with open(p, "rb") as fh:
                        state["_hashes"].add(hashlib.md5(fh.read()).hexdigest())

    t0 = time.time()
    total = 0
    for cls in args.only:
        if cls not in QUERIES:
            print(f"未知类别 {cls}，可选: {', '.join(QUERIES)}")
            continue
        total += collect(cls, QUERIES[cls], args.out, args.per_class, state, args.append)

    n, mf = write_manifest(args.out, state["rows"], args.append)
    print(f"\n本次采集 {total} 张，耗时 {time.time() - t0:.0f}s")
    print(f"来源清单 {mf}（{n} 条，与磁盘一一对应）")
    print("⚠ 下一步必须人工复查：自动门槛只能剔除小图/横幅，剔不掉'图里根本没有目标物'的错配。")


if __name__ == "__main__":
    main()
