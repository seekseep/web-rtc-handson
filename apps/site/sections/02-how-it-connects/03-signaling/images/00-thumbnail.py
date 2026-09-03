# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（居場所の交換）+ LINK（そのあと直接つながる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "最初のひと声だけ、誰かに頼む", scale="xl")

c.node(150, 175, "ブラウザ A", emoji_cp="1f310")
c.node(750, 175, "ブラウザ B", emoji_cp="1f310")
c.cloud(340, 78, 220, 104, color="teal")
c.text(450, 132, "PeerJS Cloud", scale="md", fill=PALETTE["teal"]["text"])
c.connector(196, 130, 344, 106, dash="dashed", primary=False, label="居場所", label_scale="sm")
c.connector(556, 106, 704, 130, dash="dashed", primary=False)
c.connector(216, 208, 684, 208, label="つながったら直接", label_scale="sm")

c.save("00-thumbnail.svg")
