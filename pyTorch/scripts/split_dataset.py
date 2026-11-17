#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_dataset.py —— 将图片+标签按比例划分为 train/val/test（固定随机种子，可复现）

用法:
    python split_dataset.py --images raw/images --labels raw/labels --out dataset \
        --ratio 7:2:1 --seed 42

行为:
  * 按"文件名主干"匹配图片与标签（1.jpg <-> 1.txt）
  * 图片无标签: 默认保留并生成空 txt（显式背景负样本），可用 --missing skip 跳过
  * 默认复制(原数据不动)；加 --move 改为移动
  * 输出结构: out/images/{train,val,test} + out/labels/{train,val,test}
  * 固定 seed 保证每次划分结果一致 —— 对比实验必须用同一份划分
"""
import argparse
import os
import random
import shutil
import sys

IMG_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def main() -> int:
    ap = argparse.ArgumentParser(description="YOLO 数据集划分工具")
    ap.add_argument("--images", required=True, help="源图片目录")
    ap.add_argument("--labels", required=True, help="源标签目录")
    ap.add_argument("--out", required=True, help="输出数据集根目录")
    ap.add_argument("--ratio", default="7:2:1", help="train:val:test 比例，如 7:2:1 或 0.7:0.2:0.1")
    ap.add_argument("--seed", type=int, default=42, help="随机种子（默认 42，保证可复现）")
    ap.add_argument("--missing", choices=["keep", "skip"], default="keep",
                    help="图片无标签时: keep=生成空txt保留为负样本 / skip=跳过")
    ap.add_argument("--move", action="store_true", help="移动文件而不是复制")
    args = ap.parse_args()

    # 解析比例
    try:
        parts = [float(x) for x in args.ratio.replace("：", ":").split(":")]
        if len(parts) != 3 or sum(parts) <= 0:
            raise ValueError
        s = sum(parts)
        ratios = [x / s for x in parts]
    except ValueError:
        print(f"[ERROR] --ratio 格式错误: {args.ratio}（应为 train:val:test，如 7:2:1）")
        return 1

    if not os.path.isdir(args.images):
        print(f"[ERROR] 图片目录不存在: {args.images}")
        return 1
    if not os.path.isdir(args.labels):
        print(f"[ERROR] 标签目录不存在: {args.labels}")
        return 1

    # 收集并匹配
    img_files = sorted(f for f in os.listdir(args.images) if f.lower().endswith(IMG_EXTS))
    if not img_files:
        print("[ERROR] 图片目录中没有图片")
        return 1
    items = []          # (img_path, lbl_path or None, stem)
    no_label = 0
    for f in img_files:
        stem, _ = os.path.splitext(f)
        lbl = os.path.join(args.labels, stem + ".txt")
        if os.path.isfile(lbl):
            items.append((os.path.join(args.images, f), lbl, stem))
        else:
            no_label += 1
            if args.missing == "keep":
                items.append((os.path.join(args.images, f), None, stem))
    if args.missing == "skip":
        print(f"[INFO ] 跳过 {no_label} 张无标签图片")
    elif no_label:
        print(f"[INFO ] {no_label} 张图片无标签，将生成空 txt 作为背景负样本")

    # 打乱 + 划分
    random.Random(args.seed).shuffle(items)
    n = len(items)
    n_train = int(n * ratios[0])
    n_val = int(n * ratios[1])
    splits = {
        "train": items[:n_train],
        "val": items[n_train:n_train + n_val],
        "test": items[n_train + n_val:],
    }

    # 写出
    transfer = shutil.move if args.move else shutil.copy2
    for split, files in splits.items():
        img_out = os.path.join(args.out, "images", split)
        lbl_out = os.path.join(args.out, "labels", split)
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)
        for img_path, lbl_path, stem in files:
            transfer(img_path, os.path.join(img_out, os.path.basename(img_path)))
            if lbl_path:
                transfer(lbl_path, os.path.join(lbl_out, stem + ".txt"))
            else:
                with open(os.path.join(lbl_out, stem + ".txt"), "w"):
                    pass          # 显式空标签（背景图）

    # 汇总 + 防泄漏校验
    print(f"\n划分完成（seed={args.seed}, 比例 {args.ratio}）:")
    all_stems = []
    for split, files in splits.items():
        stems = {stem for _, _, stem in files}
        all_stems.append(stems)
        print(f"  {split:5s}: {len(files):5d} 张 ({len(files) / n * 100:.1f}%)")
    leak = (all_stems[0] & all_stems[1]) | (all_stems[0] & all_stems[2]) | (all_stems[1] & all_stems[2])
    if leak:
        print(f"[ERROR] 检测到 {len(leak)} 张图片跨集合重复（数据泄漏，mAP 会虚高）: {sorted(leak)[:5]}")
        return 1
    print("[INFO ] 无跨集合重复（无数据泄漏）")
    print(f"[TIP  ] 后续所有对比实验都使用这份划分，不要改 seed 重新划分")
    return 0


if __name__ == "__main__":
    sys.exit(main())
