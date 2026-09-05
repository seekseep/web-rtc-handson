# 00-thumbnail.svg
# スキーマ: SPLITTING（聞き続ける / つないだままにする）+ BALANCE（左右に並べて対比）
# どちらも「すぐ見える」が、通り道はどちらもサーバーであることを残す

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 330)
c.text(480, 48, "聞き続けるか、つないだままにするか", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"

c.sticky(40, 76, 420, 214, color="orange")
c.text(250, 110, "ポーリング", scale="lg", fill=PALETTE["orange"]["text"])
b1 = c.node(150, 180, "", emoji_cp=BROWSER, w=76, h=64)
s1 = c.node(360, 180, "", emoji_cp=SERVER, w=76, h=64)
c.link(b1, s1, label="まだ？", label_scale="sm", offset=22)
c.link(s1, b1, label="まだ", label_scale="sm", offset=22, primary=False)
c.text(250, 262, "何秒かおきに、こちらから聞く", scale="sm")

c.sticky(500, 76, 420, 214, color="green")
c.text(710, 110, "WebSocket", scale="lg", fill=PALETTE["green"]["text"])
b2 = c.node(610, 180, "", emoji_cp=BROWSER, w=76, h=64)
s2 = c.node(820, 180, "", emoji_cp=SERVER, w=76, h=64)
c.link(s2, b2, label="届いた", label_scale="sm")
c.text(710, 262, "つないだまま。向こうから届く", scale="sm")

c.text(480, 316, "どちらも通り道はサーバー。ここが P2P との分かれ目になる", scale="sm")

c.save("00-thumbnail.svg")
