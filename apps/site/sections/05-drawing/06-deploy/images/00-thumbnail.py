# 00-thumbnail.svg
# スキーマ: CONTAINER（history に貯める）+ SOURCE-PATH-GOAL（送り直す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "あとから来た人にも、いままでの絵を見せる", scale="xl")

c.sticky(80, 108, 250, 116, color="yellow")
c.text(205, 148, "history", scale="lg", font="technical", fill=PALETTE["yellow"]["text"])
c.text(205, 180, "出した指示を貯める", scale="sm")
c.node(760, 160, "あとから来た人", emoji_cp="1f6b6", w=170, h=80)
c.connector(338, 158, 660, 158, label="つながった瞬間に、順に送り直す", label_scale="sm")
c.text(450, 258, "データチャネルは送った順に届くので、同じ絵になる", scale="sm")

c.save("00-thumbnail.svg")
