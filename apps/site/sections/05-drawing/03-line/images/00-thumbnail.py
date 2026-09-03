# 00-thumbnail.svg
# スキーマ: PART-WHOLE（曲線は細かい直線の合成）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "線は、短い直線の集まり", scale="xl")

pts = [(180, 210), (250, 150), (330, 190), (410, 120), (500, 170), (590, 110), (690, 160)]
for i in range(len(pts) - 1):
    x1, y1 = pts[i]
    x2, y2 = pts[i + 1]
    c.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3b82f6" stroke-width="7" stroke-linecap="round"/>')
for x, y in pts:
    c.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" stroke="#1d4ed8" stroke-width="3"/>')
c.text(450, 262, "点と点をつなぐ直線を、動くたびに 1 本ずつ送る", scale="sm")

c.save("00-thumbnail.svg")
