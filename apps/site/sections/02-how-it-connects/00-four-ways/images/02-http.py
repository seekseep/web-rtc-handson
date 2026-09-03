# 02-http.svg
# スキーマ: SOURCE-PATH-GOAL + CYCLE（ください → はい、これ の 1 往復）
# 2 台のブラウザが同じサーバーから同じページをもらう。ただし A と B のあいだには線が無い

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 384)
c.text(480, 46, "② サーバーに置いたファイルを、みんなが開く", scale="xl")

c.node(140, 180, "ブラウザ A", emoji_cp="1f310")
c.node(480, 180, "サーバー", emoji_cp="1f5a5")
c.node(820, 180, "ブラウザ B", emoji_cp="1f310")

c.connector(196, 152, 428, 152, label="ください", label_scale="sm")
c.connector(428, 196, 196, 196, primary=False, label="index.html", label_scale="sm")
c.connector(764, 152, 532, 152, label="ください", label_scale="sm")
c.connector(532, 196, 764, 196, primary=False, label="index.html", label_scale="sm")

c.text(480, 272, "渡したら、接続はいったん切れる", scale="sm")

c.raw('<line x1="200" y1="314" x2="760" y2="314" stroke="#cbd5e1" '
      'stroke-width="2" stroke-dasharray="7 6"/>')
c.emoji("274c", 462, 296, 36)
c.text(480, 366, "同じページをもらっただけ。A と B のあいだには何も無い", scale="sm")

c.save("02-http.svg")
