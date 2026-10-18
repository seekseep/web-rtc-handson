# 01-segments.svg
# スキーマ: PART-WHOLE（曲線＝直線の集まり）+ SOURCE-PATH-GOAL（1 本ごとに送る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)

c.text(450, 46, "指が動くたびに、前の点から今の点まで 1 本引く", scale="xl")
pts = [(120, 250), (200, 180), (290, 220), (380, 150)]
for i in range(len(pts) - 1):
    x1, y1 = pts[i]
    x2, y2 = pts[i + 1]
    c.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3b82f6" stroke-width="8" stroke-linecap="round"/>')
for x, y in pts:
    c.raw(f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" stroke="#1d4ed8" stroke-width="3"/>')
c.text(200, 300, "last", scale="sm", font="technical")
c.text(290, 300, "いまの点", scale="sm")
c.sticky(480, 130, 380, 130, color="yellow")
c.text(670, 168, "{ type: 'line',", scale="sm", font="technical", fill=PALETTE["yellow"]["text"])
c.text(670, 194, "  x1, y1, x2, y2,", scale="sm", font="technical", fill=PALETTE["yellow"]["text"])
c.text(670, 220, "  color, width }", scale="sm", font="technical", fill=PALETTE["yellow"]["text"])
c.connector(400, 195, 472, 195, label="1 本ぶん", label_scale="sm")
c.text(450, 330, "ストローク全体ではなく、線 1 本ずつ送る", scale="sm")

c.save("01-segments.svg")
