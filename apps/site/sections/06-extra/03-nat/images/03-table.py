# 03-table.svg
# スキーマ: CONTAINER（表という入れもの）+ LINK（内側の住所と外側の住所を結ぶ 1 行）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 340)
c.text(450, 48, "ルーターが覚えているのは、この表だけ", scale="xl")

c.sticky(60, 84, 780, 176, color="gray")

c.text(190, 118, "家の中の送り主", scale="sm", fill=PALETTE["gray"]["text"])
c.text(450, 118, "外に見せた送り主", scale="sm", fill=PALETTE["gray"]["text"])
c.text(710, 118, "話している相手", scale="sm", fill=PALETTE["gray"]["text"])

rows = [
    (162, "192.168.1.5:51000", "203.0.113.42:60123", "93.184.216.34:443"),
    (200, "192.168.1.8:49800", "203.0.113.42:60124", "93.184.216.34:443"),
    (238, "192.168.1.5:51001", "203.0.113.42:60125", "1.1.1.1:53"),
]
for y, inside, outside, peer in rows:
    c.text(190, y, inside, scale="sm", font="technical")
    c.text(450, y, outside, scale="sm", font="technical")
    c.text(710, y, peer, scale="sm", font="technical")

c.text(450, 292, "同じ PC でも、通信ごとに別の行になる（2 行目と 3 行目）", scale="sm")
c.text(450, 320, "用が済んだ行は、しばらくすると消える", scale="sm")

c.save("03-table.svg")
