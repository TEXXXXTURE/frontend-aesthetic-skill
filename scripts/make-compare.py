# -*- coding: utf-8 -*-
"""合成 A/B 对比图：A（无指标）| B（8 维指标注入），用于 README 展示。
来源：artifact-preview 渲染缩略图。运行：python scripts/make-compare.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

PREVIEW = r"C:\Users\A\Doubao\chats\2026-10-04\new-chat-4\.preview"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
os.makedirs(OUT, exist_ok=True)

PAIRS = [
    ("ab1", "b6428d58ea23", "0c6f6a365492"),  # 卡1 Swiss 咖啡馆
    ("ab2", "25e1e833cc42", "490385ee100c"),  # 卡2 氛围 极光电台
    ("ab3", "ee82dc958c9b", "9bec91044125"),  # 卡3 建筑静默 山间石屋
]

H = 440          # 图区高度
LABEL_H = 46     # 标签区高度
GAP = 4          # 中缝
BG = (240, 238, 229)
INK = (37, 35, 31)
ACCENT = (214, 56, 35)


def load_font(size):
    for name in ("msyh.ttc", "msyhbd.ttc", "simhei.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()


for tag, a_hash, b_hash in PAIRS:
    a = Image.open(os.path.join(PREVIEW, a_hash, "thumb.jpg")).convert("RGB")
    b = Image.open(os.path.join(PREVIEW, b_hash, "thumb.jpg")).convert("RGB")
    a = a.resize((int(a.width * H / a.height), H))
    b = b.resize((int(b.width * H / b.height), H))
    W = a.width + b.width + GAP
    canvas = Image.new("RGB", (W, H + LABEL_H), BG)
    canvas.paste(a, (0, LABEL_H))
    canvas.paste(b, (a.width + GAP, LABEL_H))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W, LABEL_H], fill=INK)
    d.rectangle([a.width, LABEL_H, a.width + GAP - 1, H + LABEL_H], fill=INK)
    font_l = load_font(20)
    font_r = load_font(20)
    d.text((18, 12), "A · 一句话方向词（无指标）", fill=BG, font=font_l)
    d.text((a.width + GAP + 18, 12), "B · 8 维指标注入", fill=ACCENT, font=font_r)
    out = os.path.join(OUT, f"compare-{tag}.png")
    canvas.save(out)
    print("saved", out, canvas.size)
