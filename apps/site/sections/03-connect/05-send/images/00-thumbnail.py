# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（色という指示が流れる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "押した色が、相手の丸に届く", scale="xl")

mine = c.ellipse(180, 160, 50, 50, color="orange")
c.text(180, 232, "自分", scale="sm")
yours = c.ellipse(720, 160, 50, 50, color="orange")
c.text(720, 232, "相手", scale="sm")
msg = c.sticky(360, 128, 180, 64, color="green")
c.text(450, 166, "{ color }", scale="md", font="technical", fill=PALETTE["green"]["text"])
c.link(mine, msg)
c.link(msg, yours)
c.text(450, 262, "送っているのは色の文字列だけ", scale="sm")

c.save("00-thumbnail.svg")
