# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（居場所の交換）+ LINK（そのあと直接つながる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 52, "最初のひと声だけ、誰かに頼む", scale="xl")

cloud = c.cloud(340, 70, 220, 100, color="teal")
c.text(450, 124, "PeerJS Cloud", scale="md", fill=PALETTE["teal"]["text"])

me = c.node(150, 205, "自分", emoji_cp="1f4bb")
you = c.node(750, 205, "相手", emoji_cp="1f4bb")

c.link(me, cloud, dash="dashed", primary=False, label="居場所", label_scale="sm")
c.link(cloud, you, dash="dashed", primary=False)
c.link(me, you, label="つながったら直接", label_scale="sm")

c.save("00-thumbnail.svg")
