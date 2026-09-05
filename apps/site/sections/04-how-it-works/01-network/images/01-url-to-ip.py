# 01-url-to-ip.svg
# スキーマ: SOURCE-PATH-GOAL（名前 → 名簿 → 番号 → 相手）+ CYCLE（引いて返る）
# URL は人間用の名前で、実際の届け先は IP アドレスとポート番号だと分かるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 440)
c.text(480, 48, "URL は人間用の名前。届け先は番号", scale="xl")

browser = c.node(160, 285, "ブラウザ", emoji_cp="1f310")
dns = c.node(480, 120, "DNS", emoji_cp="1f4d2")
server = c.node(800, 285, "サーバー", emoji_cp="1f5a5")

c.link(browser, dns, label="example.com は？", offset=30)
c.link(dns, browser, label="93.184.216.34", offset=30, primary=False)
c.link(browser, server, label="93.184.216.34 の 443 番へ")

c.text(480, 372, "https://example.com/  →  93.184.216.34:443",
       scale="lg", font="technical")
c.text(480, 416,
       "住所（IP アドレス）とポート番号がそろって、はじめて届け先になる", scale="sm")

c.save("01-url-to-ip.svg")
