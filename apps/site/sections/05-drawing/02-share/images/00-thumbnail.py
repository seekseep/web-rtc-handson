# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（指示が流れる）+ PART-WHOLE（apply と draw）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "描く指示を、相手にも送る", scale="xl")

c.sticky(70, 110, 230, 110, color="blue")
c.text(185, 152, "apply", scale="lg", font="technical", fill=PALETTE["blue"]["text"])
c.text(185, 186, "描くだけ", scale="sm")
c.sticky(340, 110, 230, 110, color="green")
c.text(455, 152, "draw", scale="lg", font="technical", fill=PALETTE["green"]["text"])
c.text(455, 186, "描いて、送る", scale="sm")
c.node(760, 160, "あいて", emoji_cp="1f310", w=120, h=80)
c.connector(340, 165, 306, 165, label="呼ぶ", label_scale="sm", primary=False)
c.connector(578, 150, 700, 150, label="送る", label_scale="sm")
c.text(450, 262, "届いた指示は apply だけ（送り返さない）", scale="sm")

c.save("00-thumbnail.svg")
