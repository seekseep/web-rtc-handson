# 03-dns.svg
# スキーマ: CYCLE（聞いて、返ってくる）+ SOURCE-PATH-GOAL（教わった住所へ送る）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 430)
c.text(480, 48, "名前を聞くと、住所が返ってくる", scale="xl")

dns = c.node(500, 128, "DNS サーバー", emoji_cp="1f5c4")
me = c.node(120, 300, "自分", emoji_cp="1f4bb")
server = c.node(830, 300, "サーバー", emoji_cp="1f5c4")

c.link(me, dns, label="example.com は?", label_scale="sm", offset=20)
c.link(dns, me, label="93.184.216.34", label_scale="sm", primary=False, offset=20)
c.link(me, server, label="教わった住所あてに送る", label_scale="sm")

c.text(480, 408, "URL のままでは送れない。住所に変えてから送る", scale="sm")

c.save("03-dns.svg")
