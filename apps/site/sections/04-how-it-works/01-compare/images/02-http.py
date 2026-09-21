# 02-http.svg
# スキーマ: SOURCE-PATH-GOAL + CYCLE（ください → はい、これ の 1 往復）
# 2 台が同じサーバーから同じページをもらう。ただし自分と相手のあいだには線が無い

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 384)
c.text(480, 46, "② サーバーに置いたファイルを、みんなが開く", scale="xl")

me = c.node(140, 180, "自分", emoji_cp="1f4bb")
server = c.node(480, 180, "サーバー", emoji_cp="1f5c4")
you = c.node(820, 180, "相手", emoji_cp="1f4bb")

# 往路と復路に同じ offset を渡すと、互いに反対側の車線へ分かれる
c.link(me, server, label="ください", label_scale="sm", offset=24)
c.link(server, me, label="index.html", label_scale="sm", offset=24, primary=False)
c.link(you, server, label="ください", label_scale="sm", offset=-24)
c.link(server, you, label="index.html", label_scale="sm", offset=-24, primary=False)

c.text(480, 272, "渡したら、接続はいったん切れる", scale="sm")

c.raw('<line x1="200" y1="314" x2="760" y2="314" stroke="#cbd5e1" '
      'stroke-width="2" stroke-dasharray="7 6"/>')
c.emoji("274c", 462, 296, 36)
c.text(480, 366, "同じページをもらっただけ。自分と相手のあいだには何も無い", scale="sm")

c.save("02-http.svg")
