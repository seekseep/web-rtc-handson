# 01-history.svg
# スキーマ: CONTAINER（history に貯める）+ SOURCE-PATH-GOAL（順に送り直す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "出した指示を貯めておいて、つながった瞬間に送り直す", scale="xl")
c.sticky(50, 90, 330, 230, color="yellow")
c.text(215, 124, "history", scale="lg", fill=PALETTE["yellow"]["text"], font="technical")
c.sticky(80, 146, 270, 42, color="green")
c.text(215, 173, "{ type: 'line', ... }", scale="sm", font="technical", fill=PALETTE["green"]["text"])
c.sticky(80, 198, 270, 42, color="green")
c.text(215, 225, "{ type: 'stamp', ... }", scale="sm", font="technical", fill=PALETTE["green"]["text"])
c.sticky(80, 250, 270, 42, color="green")
c.text(215, 277, "{ type: 'line', ... }", scale="sm", font="technical", fill=PALETTE["green"]["text"])
c.node(740, 200, "あとから来た人", emoji_cp="1f6b6", w=180, h=100)
c.connector(392, 200, 650, 200, label="貯めた順に送る", label_scale="sm")
c.text(740, 282, "同じ絵ができあがる", scale="sm")
c.text(450, 356, "データチャネルは送った順に届くので、並べ直す必要がない", scale="sm")

c.save("01-history.svg")
