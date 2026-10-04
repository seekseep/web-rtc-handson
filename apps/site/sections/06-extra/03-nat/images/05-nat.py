# 05-nat.svg
# スキーマ: CONTACT（通過点で書き換わる）+ LINK（表の 1 行が内と外を結ぶ）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 440)
c.text(480, 48, "ルーターが書き換えて、覚えておく", scale="xl")

me = c.node(150, 170, "自分", emoji_cp="1f4bb")
router = c.node(480, 170, "ルーター", emoji_cp="1f4f6")
net = c.node(810, 170, "インターネット", shape="cloud", color="gray", w=190, h=116)

c.link(me, router, label="192.168.1.5:51000", label_scale="sm", offset=24)
c.link(router, net, label="203.0.113.42:60123", label_scale="sm", offset=24)
c.link(net, router, primary=False, offset=24)
c.link(router, me, primary=False, offset=24)

table = c.sticky(270, 300, 420, 86, color="yellow")
c.text(480, 332, "覚えておく表", scale="sm", fill=PALETTE["yellow"]["text"])
c.text(480, 366, "192.168.1.5:51000 → 203.0.113.42:60123", scale="sm", font="technical")

c.link(router, table, primary=False, dash="dotted")

c.text(480, 424, "帰りはこの表を逆に引いて、家の中の機器へ渡す", scale="sm")

c.save("05-nat.svg")
