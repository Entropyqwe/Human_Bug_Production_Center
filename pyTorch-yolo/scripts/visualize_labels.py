#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
visualize_labels.py —— 把 YOLO 标注框画回原图，人工抽检标注质量

用法:
    python visualize_labels.py --images dataset/images/train --labels dataset/labels/train \
        --out check_vis --names helmet,person --num 30

说明:
  * 结果图输出到 --out 目录，逐张翻看，重点看: 框是否贴合目标、有无漏标/错标/越界
  * --num 0 表示全部绘制；>0 则随机抽样
  * --names 顺序必须与 data.yaml 中 names 完全一致
"""
import argparse
import os
import random
import sys

IMG_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# 12 种高区分度 BGR 颜色
COLORS = [
    (0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 255), (255, 0, 255),
    (255, 255, 0), (0, 165, 255), (255, 255, 255), (128, 0, 128),
    (0, 128, 255), (255, 128, 0), (128, 255, 0),
]


def main() -> int:
    try:
        import cv2
    except ImportError:
        print("[ERROR] 需要 OpenCV: pip install opencv-python")
        return 1

    ap = argparse.ArgumentParser(description="YOLO 标注可视化抽检")
    ap.add_argument("--images", required=True, help="图片目录")
    ap.add_argument("--labels", required=True, help="标签目录")
    ap.add_argument("--out", required=True, help="输出目录")
    ap.add_argument("--names", default="", help="类别名，逗号分隔，顺序同 data.yaml")
    ap.add_argument("--num", type=int, default=0, help="随机抽检张数（0=全部）")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    names = [n.strip() for n in args.names.split(",") if n.strip()]
    os.makedirs(args.out, exist_ok=True)

    img_files = sorted(f for f in os.listdir(args.images) if f.lower().endswith(IMG_EXTS))
    if not img_files:
        print(f"[ERROR] 目录无图片: {args.images}")
        return 1
    if args.num > 0 and args.num < len(img_files):
        img_files = random.Random(args.seed).sample(img_files, args.num)

    n_box, n_empty, n_missing = 0, 0, 0
    for f in img_files:
        stem, _ = os.path.splitext(f)
        img = cv2.imread(os.path.join(args.images, f))
        if img is None:
            print(f"[WARN ] 读取失败: {f}")
            continue
        h, w = img.shape[:2]
        lbl = os.path.join(args.labels, stem + ".txt")
        if os.path.isfile(lbl):
            with open(lbl, encoding="utf-8") as fh:
                lines = [ln.strip() for ln in fh if ln.strip()]
        else:
            lines, n_missing = [], n_missing + 1
        if not lines:
            n_empty += 1
            cv2.putText(img, "EMPTY (background)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        for ln in lines:
            parts = ln.split()
            if len(parts) != 5:
                continue
            cid = int(parts[0])
            cx, cy, bw, bh = map(float, parts[1:])
            x1, y1 = int((cx - bw / 2) * w), int((cy - bh / 2) * h)
            x2, y2 = int((cx + bw / 2) * w), int((cy + bh / 2) * h)
            color = COLORS[cid % len(COLORS)]
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            label = names[cid] if cid < len(names) else f"class{cid}"
            cv2.putText(img, f"{label}", (max(0, x1), max(15, y1 - 6)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)
            n_box += 1
        cv2.imwrite(os.path.join(args.out, stem + ".jpg"), img)

    print(f"[INFO ] 完成: 输出 {len(img_files)} 张到 {args.out}/ | 共 {n_box} 个框 "
          f"| 空标签 {n_empty} 张 | 缺标签 {n_missing} 张")
    print("[TIP  ] 逐张翻看：框贴合目标=合格；大量偏移/漏标=回标注工具返工")
    return 0


if __name__ == "__main__":
    sys.exit(main())
