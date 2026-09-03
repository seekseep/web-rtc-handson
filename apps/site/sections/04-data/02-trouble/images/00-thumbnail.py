# 00-thumbnail.svg
# スキーマ: BLOCKAGE（NAT が阻む）+ COUNTERFORCE（STUN / TURN で回避）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "つながらないときに何が起きているか", scale="xl")

c.node(150, 170, "ブラウザ A", emoji_cp="1f310")
c.node(750, 170, "ブラウザ B", emoji_cp="1f310")
c.emoji("1f6a7", 418, 132, 64)
c.text(450, 226, "NAT", scale="md", font="technical")
c.connector(216, 158, 404, 158, dash="dashed", primary=False)
c.connector(684, 158, 496, 158, dash="dashed", primary=False)
c.text(450, 268, "自分の住所が、自分でも分からない", scale="sm")

c.save("00-thumbnail.svg")
