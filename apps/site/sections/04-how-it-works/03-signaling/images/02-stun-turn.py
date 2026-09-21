# 02-stun-turn.svg
# スキーマ: COUNTERFORCE（STUN で回避）+ SOURCE-PATH-GOAL（TURN が中継）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 400)

c.text(450, 46, "STUN は教えるだけ、TURN は運ぶ", scale="xl")

c.sticky(50, 80, 800, 130, color="green")
c.text(84, 112, "STUN", scale="lg", align="left", fill=PALETTE["green"]["text"], font="technical")
me = c.node(250, 160, "自分", emoji_cp="1f4bb", w=110, h=70)
stun = c.node(560, 160, "STUN", emoji_cp="1fa9e", w=110, h=70)
# 往路と復路に同じ offset を渡すと、互いに反対側の車線へ分かれる
c.link(me, stun, label="私の住所は？", label_scale="sm", offset=16)
c.link(stun, me, label="ここから来ているよ", label_scale="sm", offset=16, primary=False)
c.text(760, 168, "通信は運ばない", scale="sm")

c.sticky(50, 230, 800, 130, color="orange")
c.text(120, 262, "TURN", scale="lg", align="left", fill=PALETTE["orange"]["text"], font="technical")
c.emoji("1f501", 76, 242, 34)
a = c.node(230, 310, "自分", emoji_cp="1f4bb", w=100, h=66)
turn = c.node(450, 310, "TURN", emoji_cp="1f4e6", w=110, h=66)
b = c.node(670, 310, "相手", emoji_cp="1f4bb", w=100, h=66)
c.link(a, turn)
c.link(turn, b)
c.text(790, 316, "もう P2P ではない", scale="sm")

c.save("02-stun-turn.svg")
