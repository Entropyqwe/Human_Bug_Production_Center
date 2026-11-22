#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_labels.py —— YOLO 数据集质检：data.yaml 类别配置 + 标注越界等常见问题

用法（二选一）:
    python check_labels.py --data dataset/data.yaml            # 推荐：按 data.yaml 全量检查
    python check_labels.py --images img/train --labels lbl/train --nc 3   # 按单目录检查

检查项:
  [data.yaml]  path/train/val 缺失、nc 与 names 数量不一致、类别名重复、路径不存在
  [标注文件]   字段数 != 5、class_id 越界 / 非整数、坐标越界(<0 或 >1，ultralytics 会丢弃该标签)、
               宽高 <= 0、标注框几何越界(中心+宽高超出图像，建议裁剪)、孤儿标签(有标签无图片)、
               图片缺失标签(按背景负样本统计)、空标签比例异常
  [统计]       图片/实例数量、逐类别实例分布(严重不均衡提示)

退出码: 0 = 无 ERROR(可有 WARNING)；1 = 存在 ERROR，需修复后再训练
"""
import argparse
import os
import sys
from collections import Counter

IMG_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff")
ERR, WARN, INFO = "ERROR", "WARN ", "INFO "

issues = Counter()
class_hist = Counter()      # 全局类别实例数
split_hist = {}             # 每个 split 的类别实例数


def log(level: str, msg: str) -> None:
    print(f"  [{level}] {msg}")
    issues[level.strip()] += 1


def load_names_from_yaml(path: str):
    """读取 data.yaml 的 names/nc/path/train/val/test。优先用 pyyaml，失败则退回简易解析。"""
    try:
        import yaml
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except ImportError:
        data, cur_key = {}, None
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")
                if not line.strip() or line.strip().startswith("#"):
                    continue
                indent = len(line) - len(line.lstrip())
                s = line.strip()
                if indent == 0:
                    cur_key, _, val = s.partition(":")
                    data[cur_key.strip()] = val.strip() or None
                elif cur_key and s.startswith("- ") is False and ":" in s:
                    k, _, v = s.partition(":")
                    data.setdefault(cur_key, {})[k.strip()] = v.strip()
                elif cur_key and s.startswith("- "):
                    data.setdefault(cur_key, [])
                    if isinstance(data[cur_key], dict):
                        continue
                    data[cur_key].append(s[2:].strip().strip("'\""))
    names = data.get("names")
    if isinstance(names, dict):                       # {0: person, 1: helmet, ...}
        names = [names[k] for k in sorted(names.keys())]
    return data, names


def check_data_yaml(path: str):
    print(f"\n== 检查 data.yaml: {path} ==")
    if not os.path.isfile(path):
        log(ERR, f"data.yaml 不存在: {path}")
        return None, None, []
    data, names = load_names_from_yaml(path)
    nc = data.get("nc")
    for key in ("train", "val"):
        if not data.get(key):
            log(ERR, f"data.yaml 缺少必填字段 '{key}'")
    if nc is None or names is None:
        log(ERR, "data.yaml 缺少 'nc' 或 'names' 字段")
        return data, names, []
    if int(nc) != len(names):
        log(ERR, f"nc={nc} 与 names 数量({len(names)}) 不一致 —— 类别顺序错乱的头号原因")
    if len(set(names)) != len(names):
        log(WARN, f"存在重复类别名: {[n for n in names if names.count(n) > 1]}")
    base = data.get("path", ".")
    if not os.path.isabs(base):                       # 相对路径基于 data.yaml 所在目录解析
        base = os.path.join(os.path.dirname(os.path.abspath(path)), base)
    splits = []
    for key in ("train", "val", "test"):
        rel = data.get(key)
        if not rel:
            continue
        img_dir = os.path.join(base, rel)
        splits.append(img_dir)
        if not os.path.isdir(img_dir):
            log(ERR, f"data.yaml[{key}] 指向的图片目录不存在: {img_dir}")
        else:
            n_img = sum(1 for f in os.listdir(img_dir) if f.lower().endswith(IMG_EXTS))
            print(f"  [INFO ] {key}: {img_dir} ({n_img} 张图片)")
    return data, names, splits


def check_split(img_dir: str, names, split_name: str):
    print(f"\n== 检查 {split_name}: {img_dir} ==")
    nc = len(names)
    images = sorted(f for f in os.listdir(img_dir) if f.lower().endswith(IMG_EXTS))
    # labels 目录约定: 与 images 同级，把路径中的 "images" 组件换成 "labels"（ultralytics 惯例）
    norm = os.path.normpath(img_dir)
    parts = norm.split(os.sep)
    if "images" in parts:
        parts[len(parts) - 1 - parts[::-1].index("images")] = "labels"
        lbl_dir = os.sep.join(parts)
    else:
        lbl_dir = norm
    if not os.path.isdir(lbl_dir):
        log(ERR, f"labels 目录不存在: {lbl_dir}（ultralytics 约定与 images 同级、同名替换）")
        return
    stems_img = {os.path.splitext(f)[0]: f for f in images}
    stems_lbl = {os.path.splitext(f)[0] for f in os.listdir(lbl_dir) if f.endswith(".txt")}

    n_boxes = 0
    empty_cnt = 0
    local_hist = Counter()
    for stem, img_file in stems_img.items():
        lbl = os.path.join(lbl_dir, stem + ".txt")
        if not os.path.isfile(lbl):
            log(WARN, f"图片无标签文件（将按背景负样本处理）: {img_file}")
            continue
        with open(lbl, encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        if not lines:
            empty_cnt += 1
            continue
        for i, ln in enumerate(lines, 1):
            parts = ln.split()
            if len(parts) != 5:
                log(ERR, f"{os.path.basename(lbl)} 第{i}行字段数 {len(parts)} != 5: {ln[:50]}")
                continue
            try:
                cid = int(parts[0])
                cx, cy, w, h = map(float, parts[1:])
            except ValueError:
                log(ERR, f"{os.path.basename(lbl)} 第{i}行含非法数字: {ln[:50]}")
                continue
            if cid < 0 or cid >= nc:
                log(ERR, f"{os.path.basename(lbl)} 第{i}行 class_id={cid} 越界（合法范围 0~{nc - 1}）"
                         f"—— 检查 data.yaml 类别顺序是否与标注工具一致")
                continue
            vals = (cx, cy, w, h)
            if any(v < 0 for v in vals):
                log(ERR, f"{os.path.basename(lbl)} 第{i}行存在负坐标: {ln[:50]}")
                continue
            if any(v > 1 for v in vals):
                log(ERR, f"{os.path.basename(lbl)} 第{i}行坐标 >1（未归一化或越界，ultralytics 会丢弃该标签）: {ln[:50]}")
                continue
            if w <= 0 or h <= 0:
                log(ERR, f"{os.path.basename(lbl)} 第{i}行宽高 <= 0")
                continue
            if w * h < 1e-6:
                log(WARN, f"{os.path.basename(lbl)} 第{i}行框面积极小(可能误标): w*h={w * h:.2e}")
            # 几何越界（存储值合法但框超出图像边界，常见于贴边目标，建议裁剪）
            if cx - w / 2 < 0 or cy - h / 2 < 0 or cx + w / 2 > 1 or cy + h / 2 > 1:
                log(WARN, f"{os.path.basename(lbl)} 第{i}行标注框超出图像边界，建议裁剪到 [0,1]")
            n_boxes += 1
            local_hist[cid] += 1
            class_hist[cid] += 1

    # 孤儿标签：有 txt 无图片
    for stem in sorted(stems_lbl - set(stems_img)):
        log(ERR, f"孤儿标签（无对应图片，检查文件名/扩展名大小写）: {stem}.txt")
    if images and empty_cnt / max(len(images), 1) > 0.5:
        log(WARN, f"空标签占比 {empty_cnt}/{len(images)} > 50%，疑似漏保存或漏标")
    split_hist[split_name] = local_hist
    print(f"  [INFO ] 图片 {len(images)} | 实例 {n_boxes} | 背景图 {empty_cnt}")


def main() -> int:
    ap = argparse.ArgumentParser(description="YOLO 数据集质检")
    ap.add_argument("--data", help="data.yaml 路径（推荐）")
    ap.add_argument("--images", help="图片目录（单目录检查模式）")
    ap.add_argument("--labels", help="标签目录（单目录检查模式）")
    ap.add_argument("--nc", type=int, default=None, help="类别数（单目录模式）")
    args = ap.parse_args()

    if args.data:
        data, names, splits = check_data_yaml(args.data)
        if names is None:
            return 1
        for d in splits:
            if os.path.isdir(d):
                check_split(d, names, os.path.basename(d))
    elif args.images and args.labels and args.nc is not None:
        names = [f"class_{i}" for i in range(args.nc)]
        check_split(args.images, names, "custom")
        # 单目录模式下允许 --labels 显式指定，绕过同级约定
        if os.path.normpath(args.labels) != os.path.normpath(
                args.images.replace(os.sep + "images" + os.sep, os.sep + "labels" + os.sep)):
            print("  [INFO ] --labels 与 images 同级约定路径不同，以上结果基于约定路径")
    else:
        ap.print_help()
        return 1

    # 类别分布统计
    if class_hist:
        print("\n== 逐类别实例分布 ==")
        total = sum(class_hist.values())
        for cid in range(len(names) if names else max(class_hist) + 1):
            n = class_hist.get(cid, 0)
            bar = "#" * max(1, int(n / max(class_hist.values()) * 30)) if n else ""
            print(f"  class {cid} ({names[cid] if names and cid < len(names) else '?'}): {n:5d} ({n / total * 100:.1f}%) {bar}")
        ratios = [v for v in class_hist.values() if v]
        if ratios and max(ratios) / max(min(ratios), 1) > 10:
            log(WARN, "类别严重不均衡（最多/最少 > 10 倍），考虑补采数据或加强增强")
    else:
        log(ERR, "未统计到任何标注实例，数据集可能为空")

    print("\n== 汇总 ==")
    print(f"  ERROR: {issues['ERROR']}  WARNING: {issues['WARN']}  INFO: {issues['INFO']}")
    if issues["ERROR"]:
        print("  结论: 存在必须修复的错误，请处理后重新运行")
        return 1
    print("  结论: 未发现必须修复的错误（WARNING 建议酌情处理）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
