# 01-signaling.svg
# スキーマ: SOURCE-PATH-GOAL（居場所の交換）+ LINK（直接の通り道）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)

c.text(450, 46, "つながるまでと、つながったあと", scale="xl")
cloud = c.cloud(330, 76, 240, 116, color="teal")
c.text(450, 136, "PeerJS Cloud", scale="lg", fill=PALETTE["teal"]["text"])
c.text(450, 162, "シグナリング", scale="sm")

me = c.node(150, 250, "自分", emoji_cp="1f4bb")
you = c.node(750, 250, "相手", emoji_cp="1f4bb")

c.link(me, cloud, dash="dashed", primary=False, label="SDP / 居場所", label_scale="sm")
c.link(cloud, you, dash="dashed", primary=False)
c.link(me, you, label="データチャネル（ここは直接）", label_scale="sm")

c.text(450, 336, "破線はつながるまで。実線はつながったあと", scale="sm")

c.save("01-signaling.svg")
