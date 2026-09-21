# 01-around-us.svg
# スキーマ: MERGING（用途はバラバラでも、下にあるものは 1 つ）
# 身近なサービスと、今回のお絵かきが、同じ土台に乗っていることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 348)

c.text(480, 48, "同じ技術が、いろんなところで動いている", scale="xl")

uses = [
    (150, "1f4f9", "ビデオ通話", None),
    (370, "1f465", "オンライン会議", None),
    (590, "1f4fa", "画面共有", None),
    (810, "1f3a8", "お絵かき", "green"),
]

for cx, cp, name, color in uses:
    c.node(cx, 136, "", emoji_cp=cp, w=104, h=88)
    c.text(cx, 204, name, scale="md",
           fill=PALETTE[color]["text"] if color else None)
    c.link((cx, 218), (cx, 254), primary=False)

c.sticky(110, 256, 740, 58, color="blue")
c.text(480, 293, "WebRTC", scale="lg", fill=PALETTE["blue"]["text"])

c.text(480, 338, "Google Meet も Discord も、今回のお絵かきも、下にあるのは同じもの",
       scale="sm")

c.save("01-around-us.svg")
