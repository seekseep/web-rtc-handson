# 03-host-guest.svg
# スキーマ: SOURCE-PATH-GOAL（呼び出し）+ BALANCE（open からは対等）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "役割が違うのは、つながるまで", scale="xl")
c.node(160, 150, "ホスト", emoji_cp="1f3e0")
c.text(160, 222, "new Peer('あいことば')", scale="sm", font="technical")
c.text(160, 246, "名乗って待つ", scale="sm")
c.node(740, 150, "ゲスト", emoji_cp="1f6b6")
c.text(740, 222, "new Peer()", scale="sm", font="technical")
c.text(740, 246, "名乗らず呼び出す", scale="sm")
c.connector(650, 130, 250, 130, label="peer.connect('あいことば')", label_scale="sm")
c.raw('<line x1="60" y1="288" x2="840" y2="288" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')
c.text(450, 320, "conn.on('open') から先は、どちらも同じ ready() を通る", scale="md")
c.biconnector(250, 348, 650, 348)

c.save("03-host-guest.svg")
