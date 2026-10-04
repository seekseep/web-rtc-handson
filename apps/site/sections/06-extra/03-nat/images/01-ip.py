# 01-ip.svg
# スキーマ: CYCLE（行って、返ってくる）
# 往復するので、住所は相手のぶんと自分のぶんの 2 つ要る、を見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 320)
c.text(480, 48, "往復するので、住所はふたつ要る", scale="xl")

me = c.node(180, 170, "自分", emoji_cp="1f4bb")
server = c.node(780, 170, "サーバー", emoji_cp="1f5c4")

c.link(me, server, label="サーバーの住所あて", label_scale="sm", offset=24)
c.link(server, me, label="自分の住所あて", label_scale="sm", primary=False, offset=24)

c.text(480, 296, "この住所が IP アドレス。片方だけでは返事が返らない", scale="sm")

c.save("01-ip.svg")
