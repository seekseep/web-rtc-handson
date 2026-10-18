# 00-thumbnail.svg
# スキーマ: ITERATION（同じ操作を繰り返すたびに状態が移る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "押すたびに、色が変わる", scale="xl")

c.sticky(60, 130, 170, 60, color="blue")
c.text(145, 167, "ひからせる", scale="md", fill=PALETTE["blue"]["text"])
c.ellipse(380, 160, 50, 50, color="pink")
c.text(380, 238, "1 回目", scale="sm")
c.ellipse(560, 160, 50, 50, color="teal")
c.text(560, 238, "2 回目", scale="sm")
c.ellipse(740, 160, 50, 50, color="purple")
c.text(740, 238, "3 回目", scale="sm")
c.connector(240, 160, 322, 160)
c.connector(436, 160, 504, 160, primary=False)
c.connector(616, 160, 684, 160, primary=False)

c.text(450, 272, "色相だけを乱数で振る（hsl）", scale="sm")

c.save("00-thumbnail.svg")
