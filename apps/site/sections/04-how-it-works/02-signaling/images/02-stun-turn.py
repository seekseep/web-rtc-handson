# 02-stun-turn.svg
# スキーマ: COUNTERFORCE（STUN で回避）+ SOURCE-PATH-GOAL（TURN が中継）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 400)

c.text(450, 46, "STUN は教えるだけ、TURN は運ぶ", scale="xl")
c.sticky(50, 80, 800, 130, color="green")
c.text(84, 112, "STUN", scale="lg", align="left", fill=PALETTE["green"]["text"], font="technical")
c.node(250, 160, "ブラウザ", emoji_cp="1f310", w=110, h=70)
c.node(560, 160, "STUN", emoji_cp="1fa9e", w=110, h=70)
c.connector(306, 146, 504, 146, label="私の住所は？", label_scale="sm")
c.connector(504, 178, 306, 178, primary=False, label="ここから来ているよ", label_scale="sm")
c.text(760, 168, "通信は運ばない", scale="sm")
c.sticky(50, 230, 800, 130, color="orange")
c.text(120, 262, "TURN", scale="lg", align="left", fill=PALETTE["orange"]["text"], font="technical")
c.emoji("1f501", 76, 242, 34)
c.node(230, 310, "A", emoji_cp="1f310", w=100, h=66)
c.node(450, 310, "TURN", emoji_cp="1f4e6", w=110, h=66)
c.node(670, 310, "B", emoji_cp="1f310", w=100, h=66)
c.connector(280, 300, 400, 300)
c.connector(500, 300, 620, 300)
c.text(790, 316, "もう P2P ではない", scale="sm")

c.save("02-stun-turn.svg")
