# 00-thumbnail.svg
# スキーマ: CONTAINER（家の中）+ SOURCE-PATH-GOAL（外へ出て、戻ってくる）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 50, "出ていくときに書き換え、帰りに書き戻す", scale="xl")

home = c.node(160, 165, "家の中の PC", emoji_cp="1f4bb", color="blue")
router = c.node(450, 165, "ルーター", emoji_cp="1f4e1", color="yellow")
net = c.node(760, 165, "インターネット", shape="cloud", color="gray", w=190, h=116)

c.link(home, router, label="192.168.1.5", label_scale="sm", offset=22)
c.link(router, net, label="203.0.113.42", label_scale="sm", offset=22)
c.link(net, router, primary=False, offset=22)
c.link(router, home, primary=False, offset=22)

c.text(450, 278, "書き換えた相手を 1 行の表に覚えておくから、帰りの便が戻れる", scale="sm")

c.save("00-thumbnail.svg")
