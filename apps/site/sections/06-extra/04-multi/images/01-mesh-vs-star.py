# 01-mesh-vs-star.svg
# スキーマ: CENTER-PERIPHERY（スター）vs LINK の総当たり（メッシュ）

import math
import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

N = 5
R = 74


def ring(cx, cy, n=N, r=R):
    """中心 (cx, cy) の円周上に n 個の点を返す（頂点が上から始まる）。"""
    return [
        (cx + r * math.sin(2 * math.pi * i / n), cy - r * math.cos(2 * math.pi * i / n))
        for i in range(n)
    ]


def dot(c, x, y, color):
    p = PALETTE[color]
    c.raw(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="{p["bg"]}" '
          f'stroke="{p["border"]}" stroke-width="3"/>')


def link(c, a, b, color="#94a3b8"):
    c.raw(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
          f'stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>')


c = Canvas(900, 380)
c.text(450, 50, "つなぎ方は 2 通りある", scale="xl")

c.sticky(50, 84, 380, 240, color="purple")
c.text(240, 122, "メッシュ", scale="lg", fill=PALETTE["purple"]["text"])
mesh = ring(240, 216)
for i in range(N):
    for j in range(i + 1, N):
        link(c, mesh[i], mesh[j])
for x, y in mesh:
    dot(c, x, y, "purple")
c.text(240, 314, "5 人で 10 本。落ちても平気", scale="sm", fill=PALETTE["purple"]["text"])

c.sticky(470, 84, 380, 240, color="teal")
c.text(660, 122, "スター", scale="lg", fill=PALETTE["teal"]["text"])
star = ring(660, 216, n=4, r=R)
for p in star:
    link(c, (660, 216), p)
for x, y in star:
    dot(c, x, y, "teal")
dot(c, 660, 216, "orange")
c.text(660, 314, "5 人で 4 本。中心が落ちると全滅", scale="sm", fill=PALETTE["teal"]["text"])

c.text(450, 356, "ここではスターにする。名簿を作らなくて済むから", scale="sm")

c.save("01-mesh-vs-star.svg")
