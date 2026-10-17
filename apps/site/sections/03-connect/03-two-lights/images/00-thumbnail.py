# 00-thumbnail.svg
# スキーマ: PART-WHOLE（同じ型の部品が 2 つ並ぶ）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 322)
c.text(450, 50, "ライトを 2 つ、ボタンも 2 つ", scale="xl")

c.ellipse(300, 125, 52, 52, color="yellow")
c.text(300, 198, "じぶん", scale="md")
c.ellipse(620, 125, 52, 52, color="gray")
c.text(620, 198, "あいて", scale="md")

c.sticky(215, 220, 170, 54, color="blue")
c.text(300, 254, "ひからせる", scale="md", fill=PALETTE["blue"]["text"])
c.sticky(505, 220, 230, 54, color="gray")
c.text(620, 254, "あいてをひからせる", scale="md", fill=PALETTE["gray"]["text"])

c.text(450, 300, "右のボタンは練習用。次の節で、押す係を相手にゆずる", scale="sm")

c.save("00-thumbnail.svg")
