# 01-instruction-size.svg
# スキーマ: SCALE（指示に入れる情報の量は、命令によって違う）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 320)
c.text(450, 48, "指示に入れるのは、その命令に必要な情報だけ", scale="xl")

c.sticky(70, 96, 360, 160, color="blue")
c.text(250, 128, "line", scale="lg", font="technical", fill=PALETTE["blue"]["text"])
c.text(250, 162, "x1, y1, x2, y2", scale="sm", font="technical")
c.text(250, 188, "color, width", scale="sm", font="technical")
c.text(250, 226, "どこに・何色で・どの太さで", scale="sm")

c.sticky(470, 96, 360, 160, color="yellow")
c.text(650, 128, "clear", scale="lg", font="technical", fill=PALETTE["yellow"]["text"])
c.text(650, 172, "（ほかに何もいらない）", scale="sm")
c.text(650, 226, "「ぜんぶ消して」だけで伝わる", scale="sm")

c.text(450, 296, "足りないと画面がズレる。多すぎても意味がない。", scale="sm")

c.save("01-instruction-size.svg")
