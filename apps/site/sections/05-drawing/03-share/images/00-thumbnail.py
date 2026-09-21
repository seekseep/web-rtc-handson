# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（指示が流れる）+ PART-WHOLE（apply と draw）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "描く指示を、相手にも送る", scale="xl")

apply_box = c.sticky(70, 110, 230, 110, color="blue")
c.text(185, 152, "apply", scale="lg", font="technical", fill=PALETTE["blue"]["text"])
c.text(185, 186, "描くだけ", scale="sm")
draw_box = c.sticky(340, 110, 230, 110, color="green")
c.text(455, 152, "draw", scale="lg", font="technical", fill=PALETTE["green"]["text"])
c.text(455, 186, "描いて、送る", scale="sm")
you = c.node(760, 165, "相手", emoji_cp="1f4bb", w=120, h=80)

c.link(draw_box, apply_box, label="呼ぶ", label_scale="sm", primary=False)
c.link(draw_box, you, label="送る", label_scale="sm")
c.text(450, 262, "届いた指示は apply だけ（送り返さない）", scale="sm")

c.save("00-thumbnail.svg")
