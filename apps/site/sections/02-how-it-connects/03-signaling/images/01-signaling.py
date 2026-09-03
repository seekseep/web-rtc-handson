# 01-signaling.svg
# スキーマ: SOURCE-PATH-GOAL（居場所の交換）+ LINK（直接の通り道）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)

c.text(450, 46, "つながるまでと、つながったあと", scale="xl")
c.cloud(330, 76, 240, 116, color="teal")
c.text(450, 136, "PeerJS Cloud", scale="lg", fill=PALETTE["teal"]["text"])
c.text(450, 162, "シグナリング", scale="sm")
c.node(150, 250, "ブラウザ A", emoji_cp="1f310")
c.node(750, 250, "ブラウザ B", emoji_cp="1f310")
c.connector(196, 208, 338, 150, dash="dashed", primary=False, label="SDP / 居場所", label_scale="sm")
c.connector(562, 150, 704, 208, dash="dashed", primary=False)
c.connector(220, 288, 680, 288, label="データチャネル（ここは直接）", label_scale="sm")
c.text(450, 336, "破線はつながるまで。実線はつながったあと", scale="sm")

c.save("01-signaling.svg")
