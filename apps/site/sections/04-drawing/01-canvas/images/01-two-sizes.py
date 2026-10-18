# 01-two-sizes.svg
# スキーマ: SCALE（同じものが大きさ違いで現れる）+ PART-WHOLE（1 枚のキャンバスが 2 つの大きさを持つ）
# この節のつまずきの「前提」だけを描く図。中の解像度は固定、見た目だけが端末で変わる。

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE, INK_SCALE

c = Canvas(960, 470)


def grid(x, y, w, h, color, cols=8, rows=6):
    """キャンバスの「中の方眼」。3 つの箱で同じ 8 x 6 にして、
    大きさが違っても中身は同じ刻みだと分かるようにする。"""
    stroke = PALETTE[color]["border"]
    for i in range(1, cols):
        gx = x + w * i / cols
        c.raw(f'<line x1="{gx:.1f}" y1="{y:.1f}" x2="{gx:.1f}" y2="{y + h:.1f}" '
              f'stroke="{stroke}" stroke-width="1" opacity="0.3"/>')
    for j in range(1, rows):
        gy = y + h * j / rows
        c.raw(f'<line x1="{x:.1f}" y1="{gy:.1f}" x2="{x + w:.1f}" y2="{gy:.1f}" '
              f'stroke="{stroke}" stroke-width="1" opacity="0.3"/>')


def stamp(x, y, w, h, size):
    """同じ場所（方眼の同じマス）に 🐱 を置いて、中身が同じことを見せる。"""
    c.emoji("1f431", x + w * 0.6875 - size / 2, y + h * 0.4167 - size / 2, size)


c.text(480, 46, "1 枚のキャンバスに、大きさが 2 つある", scale="xl")

# --- ① 中の解像度 ---------------------------------------------------------
c.text(272, 96, "① 中の解像度 — いつも 800 x 600", scale="md", fill=PALETTE["blue"]["text"])

inner = c.sticky(132, 146, 280, 210, color="blue", rx=8)
grid(132, 146, 280, 210, "blue")
stamp(132, 146, 280, 210, 40)
c.link((132, 126), (412, 126), both=True, label="800", label_scale="sm",
       label_font="technical", primary=False)
c.link((112, 146), (112, 356), both=True, label="600", label_scale="sm",
       label_font="technical", primary=False)

c.text(272, 390, '<canvas width="800" height="600">', scale="sm", font="technical")
c.text(272, 418, "絵を描くときの座標。\n端末が変わっても、この数は動かない", scale="sm")

# --- ② 見た目の大きさ -----------------------------------------------------
c.text(708, 96, "② 見た目の大きさ — 端末しだい", scale="md", fill=PALETTE["green"]["text"])

c.text(632, 176, "パソコン", scale="sm", fill=PALETTE["green"]["text"])
pc = c.sticky(520, 188, 224, 168, color="green", rx=8)
grid(520, 188, 224, 168, "green")
stamp(520, 188, 224, 168, 32)
c.text(632, 390, "rect.width = 600", scale="sm", font="technical")

c.text(860, 248, "スマホ", scale="sm", fill=PALETTE["green"]["text"])
sp = c.sticky(796, 260, 128, 96, color="green", rx=8)
grid(796, 260, 128, 96, "green")
stamp(796, 260, 128, 96, 18)
c.text(860, 390, "rect.width = 350", scale="sm", font="technical")

c.text(708, 418, "CSS で縮めて表示しているだけ。\nクリックの event.clientX はこちらの px で届く", scale="sm")

c.link(inner, pc, label="縮めて表示", label_scale="sm", start="e", end="w", dash="dashed")

c.save("01-two-sizes.svg")
