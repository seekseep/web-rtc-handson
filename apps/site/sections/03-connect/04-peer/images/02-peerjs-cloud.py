# 02-peerjs-cloud.svg
# スキーマ: SOURCE-PATH-GOAL（挨拶を送ると名前が返ってくる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "PeerJS Cloud は登録もキーもいらない", scale="xl")

browser = c.node(190, 165, "ブラウザ", emoji_cp="1f310")
cloud = c.cloud(560, 100, 300, 150, color="teal")
c.text(710, 168, "PeerJS Cloud", scale="lg", fill=PALETTE["teal"]["text"])
c.text(710, 196, "0.peerjs.com", scale="sm", font="technical")
c.link(browser, cloud, label="new Peer()", label_scale="sm", offset=28)
c.link(cloud, browser, label="名前を配る", label_scale="sm", primary=False, offset=28)

c.save("02-peerjs-cloud.svg")
