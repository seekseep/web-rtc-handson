# 02-coordinates.svg
# スキーマ: SOURCE-PATH-GOAL（画面の px → 割合 → 中の座標）+ LINK（割合が 2 つの大きさを結ぶ）
# 01-two-sizes.svg で見せた前提の続き。割り戻しの途中に「割合」が挟まることを見せる。

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE, INK_SCALE

c = Canvas(960, 410)


def grid(x, y, w, h, color, cols=8, rows=6):
    """01-two-sizes.svg と同じ 8 x 6 の方眼。2 つの箱が同じものだと分かるようにする。"""
    stroke = PALETTE[color]["border"]
    for i in range(1, cols):
        gx = x + w * i / cols
        c.raw(f'<line x1="{gx:.1f}" y1="{y:.1f}" x2="{gx:.1f}" y2="{y + h:.1f}" '
              f'stroke="{stroke}" stroke-width="1" opacity="0.3"/>')
    for j in range(1, rows):
        gy = y + h * j / rows
        c.raw(f'<line x1="{x:.1f}" y1="{gy:.1f}" x2="{x + w:.1f}" y2="{gy:.1f}" '
              f'stroke="{stroke}" stroke-width="1" opacity="0.3"/>')


c.text(480, 46, "画面の px を割合に直してから、中の座標に戻す", scale="xl")

# --- 画面でタップした場所 -------------------------------------------------
# 箱の大きさも 01-two-sizes.svg にそろえる（見た目のほうが小さい）
c.text(130, 112, "スマホの画面（350px）", scale="sm", fill=PALETTE["green"]["text"])
screen = c.sticky(60, 141, 140, 105, color="green", rx=8)
grid(60, 141, 140, 105, "green")
c.raw('<circle cx="200" cy="194" r="9" fill="#e5484d"/>')
c.text(130, 286, "clientX - rect.left", scale="sm", font="technical")
c.text(130, 314, "350", scale="md", font="technical", fill=INK_SCALE["ink"])

# --- 割合（ここが要） -----------------------------------------------------
ratio = c.sticky(410, 154, 140, 80, color="yellow")
c.text(480, 186, "どこまで来たか", scale="sm", fill=PALETTE["yellow"]["text"])
c.text(480, 214, "割合", scale="md", fill=PALETTE["yellow"]["text"])
c.text(480, 286, "端末が変わっても同じ値", scale="sm")
c.text(480, 314, "1.0", scale="md", font="technical", fill=INK_SCALE["ink"])

# --- キャンバスの中 -------------------------------------------------------
c.text(815, 112, "キャンバスの中（800 x 600）", scale="sm", fill=PALETTE["blue"]["text"])
inner = c.sticky(730, 130, 170, 128, color="blue", rx=8)
grid(730, 130, 170, 128, "blue")
# 割り戻した結果＝タップした右端。割らずに 350 のまま描くと 350/800＝44% の位置。
c.emoji("274c", 793, 177, 22)
c.text(804, 232, "350", scale="sm", font="technical", fill=PALETTE["red"]["text"])
c.raw('<circle cx="900" cy="188" r="9" fill="#e5484d"/>')
c.text(876, 232, "800", scale="sm", font="technical", fill=PALETTE["blue"]["text"])
c.text(815, 286, "タップした右端に出る", scale="sm")
c.text(815, 314, "800", scale="md", font="technical", fill=INK_SCALE["ink"])

c.link(screen, ratio, label="÷ rect.width", label_scale="sm",
       label_font="technical", start="e", end="w", clearance=14)
c.link(ratio, inner, label="× canvas.width", label_scale="sm",
       label_font="technical", start="e", end="w")

c.text(480, 376, "割らずに 350 のまま描くと、❌ の位置（中の 44%）に出てしまう",
       scale="sm", fill=PALETTE["red"]["text"])

c.save("02-coordinates.svg")
