# 00-thumbnail.svg
# スキーマ: CENTER-PERIPHERY（ホストが中心）+ SOURCE-PATH-GOAL（中継）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 370)
c.text(450, 50, "ホストが受け取って、ほかの全員に配る", scale="xl")

c.node(450, 140, "ホスト", emoji_cp="1f3e0", label_scale="label")

c.node(160, 292, "ゲスト A", emoji_cp="1f310", label_scale="label")
c.node(740, 292, "ゲスト B", emoji_cp="1f310", label_scale="label")

c.biconnector(390, 170, 214, 242, primary=True)
c.biconnector(510, 170, 686, 242, primary=True)

c.text(450, 268, "ゲスト同士は直接つながらない", scale="sm")
c.text(450, 296, "ホストを通って、絵がそろう", scale="sm")

c.save("00-thumbnail.svg")
