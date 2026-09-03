# 00-thumbnail.svg
# スキーマ: SPLITTING（2つのやり方を左右に並べる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "真ん中を通るか、直接つなぐか", scale="xl")

c.text(230, 100, "いつもの Web", scale="lg")
c.emoji("1f310", 118, 130, 52)
c.emoji("1f5a5", 204, 130, 52)
c.emoji("1f310", 290, 130, 52)
c.connector(174, 156, 200, 156, primary=False)
c.connector(260, 156, 286, 156, primary=False)
c.text(230, 222, "必ずサーバーを経由する", scale="sm")
c.raw('<line x1="450" y1="88" x2="450" y2="248" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')
c.text(670, 100, "今回つくるもの", scale="lg")
c.emoji("1f310", 560, 130, 52)
c.emoji("1f310", 730, 130, 52)
c.connector(618, 148, 726, 148)
c.connector(726, 176, 618, 176, primary=False)
c.text(670, 222, "ブラウザ同士が直接つながる", scale="sm")

c.save("00-thumbnail.svg")
