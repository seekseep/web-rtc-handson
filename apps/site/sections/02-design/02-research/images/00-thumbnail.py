# 00-thumbnail.svg
# スキーマ: BLOCKAGE + SOURCE-PATH-GOAL（作る前に立ちはだかる 2 つを、探して埋める）
# 調査の節の入口。足りないものが 2 つあり、それを自前で作らない道を探したと見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(940, 400)
c.text(470, 46, "足りない 2 つを、どう埋めるか", scale="xl")

connect = c.node(200, 155, "つなぐしくみ", emoji_cp="1f6a7", w=220, h=88)  # 🚧
publish = c.node(200, 285, "公開する場所", emoji_cp="1f6a7", w=220, h=88)  # 🚧
search = c.node(680, 220, "あるものを探す", emoji_cp="1f50d", w=230, h=96)  # 🔍

c.link(connect, search)
c.link(publish, search)

c.text(470, 380, "自分で作ると、アプリを作る時間が無くなってしまう", scale="sm")

c.save("00-thumbnail.svg")
