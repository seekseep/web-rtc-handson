# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（名前 → 番号 → 届く）+ BLOCKAGE（逆向きには届かない）
# 「サーバーには届く。でもブラウザには届かない」という非対称をひと目で見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 330)
c.text(480, 48, "ブラウザには、外から呼びかけられない", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"
ROUTER = "1f4e1"

cols = [
    (165, "blue", "① 名前を番号に直す", "example.com → 93.184.216.34"),
    (480, "blue", "② その番号へ届ける", "サーバーには住所がある"),
    (795, "red", "③ 逆はできない", "ブラウザには住所が無い"),
]

for cx, color, head, foot in cols:
    c.sticky(cx - 145, 76, 290, 200, color=color)
    c.text(cx, 108, head, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 254, foot, scale="sm")

b1 = c.node(105, 180, "", emoji_cp=BROWSER, w=76, h=64)
d1 = c.node(225, 180, "", emoji_cp="1f4d2", w=76, h=64)
c.link(b1, d1, primary=False)

b2 = c.node(420, 180, "", emoji_cp=BROWSER, w=76, h=64)
s2 = c.node(540, 180, "", emoji_cp=SERVER, w=76, h=64)
c.link(b2, s2)

s3 = c.node(735, 180, "", emoji_cp=SERVER, w=76, h=64)
b3 = c.node(855, 180, "", emoji_cp=BROWSER, w=76, h=64)
c.link(s3, b3, primary=False, dash="dashed", head=False)
c.emoji("274c", 780, 164, 30)

c.text(480, 316, "だから P2P は、まず「相手の住所」から始めることになる", scale="sm")

c.save("00-thumbnail.svg")
