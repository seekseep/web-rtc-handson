# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL + SCALE（小さいものから、大きいものへ）
# 設計の節の入口。作るものは 2 つで、順番があることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(860, 340)
c.text(430, 46, "小さいものから、育てていく", scale="xl")

light = c.node(190, 190, "ボタンで光る", emoji_cp="1f4a1", w=190, h=96)  # 💡
draw = c.node(660, 190, "いっしょにお絵かき", emoji_cp="1f3a8", w=230, h=96)  # 🎨

c.link(light, draw, label="同じしくみのまま")

c.text(430, 316, "先に通信を確かめてから、機能を足していく", scale="sm")

c.save("00-thumbnail.svg")
