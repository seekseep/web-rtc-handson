# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（押す → 塗られる）+ 状態の前後

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "押したら、丸が光る", scale="xl")

c.ellipse(180, 160, 50, 50, color="gray")
c.text(180, 238, "押す前", scale="sm")
c.sticky(365, 130, 170, 60, color="blue")
c.text(450, 167, "ひからせる", scale="md", fill=PALETTE["blue"]["text"])
c.ellipse(720, 160, 50, 50, color="yellow")
c.text(720, 238, "押したあと", scale="sm")
c.connector(236, 160, 356, 160)
c.connector(544, 160, 664, 160)

c.text(450, 272, "部品をつかむ → 押されたら塗る。まずはこれだけ", scale="sm")

c.save("00-thumbnail.svg")
