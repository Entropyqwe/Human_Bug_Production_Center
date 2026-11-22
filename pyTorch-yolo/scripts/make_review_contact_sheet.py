#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把 data/raw_v3/<类别>/ 下的图片拼成缩略图总览，用于人工快速复查。

    python scripts/make_review_contact_sheet.py

输出 data/raw_v3/review/<类别>.png，每张图左上角标注文件名编号。
复查时只记编号，删图用：
    rm data/raw_v3/phone/007.jpg   # 举例
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "data", "raw_v3")
OUT = os.path.join(RAW, "review")
THUMB_W, THUMB_H, PAD, LABEL = 300, 225, 6, 22
COLS = 5


def sheet(cls):
    d = os.path.join(RAW, cls)
    if not os.path.isdir(d):
        return None
    files = sorted(f for f in os.listdir(d) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    if not files:
        return None
    rows = (len(files) + COLS - 1) // COLS
    cw, ch = THUMB_W + PAD * 2, THUMB_H + LABEL + PAD * 2
    canvas = Image.new("RGB", (COLS * cw, rows * ch), (24, 24, 24))
    dr = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.load_default(size=LABEL)
    except Exception:
        font = None
    for i, f in enumerate(files):
        x, y = (i % COLS) * cw + PAD, (i // COLS) * ch + PAD
        try:
            with Image.open(os.path.join(d, f)) as im:
                im = im.convert("RGB")
                im.thumbnail((THUMB_W, THUMB_H))
                canvas.paste(im, (x, y + LABEL))
        except Exception as e:
            dr.rectangle([x, y + LABEL, x + THUMB_W, y + LABEL + THUMB_H], outline=(200, 60, 60))
            dr.text((x + 4, y + LABEL + 4), f"读取失败 {type(e).__name__}", fill=(240, 120, 120), font=font)
        dr.text((x + 2, y), os.path.splitext(f)[0], fill=(255, 220, 80), font=font)
    canvas.save(os.path.join(OUT, f"{cls}.png"))
    return len(files), canvas.size


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for cls in ("phone", "bottle", "charger", "key", "cup"):
        r = sheet(cls)
        if r:
            total += r[0]
            print(f"  {cls:8s} {r[0]:3d} 张 → review/{cls}.png  ({r[1][0]}x{r[1][1]})")
    print(f"\n共 {total} 张已拼版，打开 {OUT} 逐类扫一遍，只记要删的编号。")
