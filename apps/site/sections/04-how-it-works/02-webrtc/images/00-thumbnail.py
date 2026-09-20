# 00-thumbnail.svg
# スキーマ: SPLITTING（2つのやり方を左右に並べる）
# どちらも両端にいるのは人。真ん中にサーバーが居るかどうかだけが違う

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 52, "真ん中を通るか、直接つなぐか", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"

c.text(230, 104, "いつもの Web", scale="lg", fill=PALETTE["gray"]["text"])
c.emoji("1f9d1", 60, 164, 36)
ba = c.node(148, 168, "", emoji_cp=BROWSER, w=58, h=48)
sv = c.node(230, 168, "", emoji_cp=SERVER, w=58, h=48)
bb = c.node(312, 168, "", emoji_cp=BROWSER, w=58, h=48)
c.emoji("1f9d1", 368, 164, 36)
c.link(ba, sv, primary=False)
c.link(sv, bb, primary=False)
c.text(230, 244, "必ずサーバーを経由する", scale="sm")

c.raw('<line x1="450" y1="92" x2="450" y2="262" '
      'stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')

c.text(670, 104, "03 章で作ったもの", scale="lg", fill=PALETTE["green"]["text"])
c.emoji("1f9d1", 500, 164, 36)
ca = c.node(588, 168, "", emoji_cp=BROWSER, w=58, h=48)
cb = c.node(752, 168, "", emoji_cp=BROWSER, w=58, h=48)
c.emoji("1f9d1", 804, 164, 36)
c.link(ca, cb, both=True)
c.text(670, 244, "ブラウザ同士が直接つながる", scale="sm")

c.text(450, 286, "この節で見るのは、右がなぜ難しいのか", scale="sm")

c.save("00-thumbnail.svg")
