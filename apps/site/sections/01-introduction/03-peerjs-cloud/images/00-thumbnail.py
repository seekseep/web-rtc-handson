# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（挨拶を送ると名前が返ってくる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "PeerJS Cloud は登録もキーもいらない", scale="xl")

c.node(190, 165, "ブラウザ", emoji_cp="1f310")
c.cloud(560, 100, 300, 150, color="teal")
c.text(710, 168, "PeerJS Cloud", scale="lg", fill=PALETTE["teal"]["text"])
c.text(710, 196, "0.peerjs.com", scale="sm", font="technical")
c.connector(290, 140, 560, 140, label="new Peer()", label_scale="sm")
c.connector(560, 200, 290, 200, label="名前を配る", label_scale="sm", primary=False)

c.save("00-thumbnail.svg")
