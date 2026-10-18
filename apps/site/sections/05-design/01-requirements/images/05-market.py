# 05-market.svg
# スキーマ: CONTAINER + NEAR-FAR（四角いマスとマスなしばかりの棚の外に、六角形だけが無い）
# 似たアプリを調べると、まだ誰も作っていない場所が見えてくることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE, INK_SCALE

c = Canvas(1100, 470)
c.text(550, 46, "似たアプリに、六角形のマスは無かった", scale="xl")

c.sticky(40, 86, 700, 300, color="gray")
c.text(72, 126, "App Store で 20 本くらい", scale="lg", align="left",
       fill=PALETTE["blue"]["text"])

SIZE = 96
LINE = INK_SCALE["gray"]
DOTS = ["red", "blue", "green", "yellow"]


def grid_tile(x, y):
    """四角いマスのアプリ。3 × 3 の方眼を描く。"""
    c.sticky(x, y, SIZE, SIZE, color="gray", rx=8, weight="thin")
    for i in (1, 2):
        d = SIZE * i / 3
        c.raw(f'<line x1="{x + d:g}" y1="{y + 8:g}" x2="{x + d:g}" y2="{y + SIZE - 8:g}" '
              f'stroke="{LINE}" stroke-width="1.5"/>')
        c.raw(f'<line x1="{x + 8:g}" y1="{y + d:g}" x2="{x + SIZE - 8:g}" y2="{y + d:g}" '
              f'stroke="{LINE}" stroke-width="1.5"/>')


def free_tile(x, y):
    """マスのないアプリ。白い紙に点だけが置いてある。"""
    c.sticky(x, y, SIZE, SIZE, color="gray", rx=8, weight="thin")
    for (dx, dy), color in zip([(0.25, 0.3), (0.72, 0.25), (0.35, 0.75), (0.75, 0.7)], DOTS):
        c.raw(f'<circle cx="{x + SIZE * dx:g}" cy="{y + SIZE * dy:g}" r="7" '
              f'fill="{PALETTE[color]["border"]}"/>')


kinds = ["grid", "grid", "free", "grid", "grid",
         "grid", "free", "grid", "grid", "free"]
for i, kind in enumerate(kinds):
    x = 80 + (i % 5) * 126
    y = 156 + (i // 5) * 114
    (grid_tile if kind == "grid" else free_tile)(x, y)

# 棚の外に、六角形の空き。点線で「無い」ことを見せる
c.text(910, 126, "どこにも無い", scale="lg", fill=PALETTE["yellow"]["text"])
c.hexagon(830, 180, 160, 138, color="yellow", dash="dashed")
c.text(910, 256, "六角形のマス", scale="md")

c.text(550, 440, "四角いマスか、マスがないものばかり。工夫する場所を、マスの形に決めた", scale="sm")

c.save("05-market.svg")
