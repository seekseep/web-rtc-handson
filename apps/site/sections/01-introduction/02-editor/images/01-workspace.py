# 01-workspace.svg
# スキーマ: CONTAINER（app/ の中に 3 ファイル）+ LINK（index.html が 2 つを読み込む）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "app/ フォルダの中に、3 つのファイルを作る", scale="xl")

app = c.sticky(60, 80, 440, 270, color="yellow")
c.emoji("1f4c1", 86, 96, 40)
c.text(140, 124, "app/", scale="lg", align="left", fill=PALETTE["yellow"]["text"], font="technical")

c.sticky(86, 150, 388, 58, color="blue")
c.emoji("1f310", 104, 162, 34)
c.text(150, 176, "index.html", scale="md", align="left", fill=PALETTE["blue"]["text"], font="technical")
c.text(150, 198, "画面の骨組み", scale="sm", align="left")

c.sticky(86, 218, 388, 58, color="purple")
c.emoji("1f3a8", 104, 230, 34)
c.text(150, 244, "style.css", scale="md", align="left", fill=PALETTE["purple"]["text"], font="technical")
c.text(150, 266, "見た目", scale="sm", align="left")

c.sticky(86, 286, 388, 58, color="orange")
c.emoji("1f4c4", 104, 298, 34)
c.text(150, 312, "main.js", scale="md", align="left", fill=PALETTE["orange"]["text"], font="technical")
c.text(150, 334, "動き", scale="sm", align="left")

peerjs = c.cloud(610, 130, 260, 130, color="teal")
c.text(740, 190, "PeerJS 本体", scale="lg", fill=PALETTE["teal"]["text"])
c.text(740, 216, "CDN から読み込む", scale="sm")
c.link(app, peerjs, label="読み込む", label_scale="sm", start="e", end="w")
c.text(700, 300, "インストールは不要", scale="sm")

c.save("01-workspace.svg")
