# 01-what-matters.svg
# スキーマ: CENTER-PERIPHERY（真ん中の決めごとを、3 つのものさしが取り囲む）
# 題材を選ぶときに何を見ていたのかを、判断基準として並べる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 440)
c.text(480, 46, "何を作るかは、この 3 つで決めた", scale="xl")

core = c.sticky(370, 158, 220, 120, color="yellow")
c.text(480, 208, "作るもの", scale="lg")

wow = c.node(140, 150, "見てて凄い", emoji_cp="1f440", w=170, h=88)  # 👀
take = c.node(820, 150, "持ち帰れる", emoji_cp="1f381", w=170, h=88)  # 🎁
only = c.node(480, 356, "これでしか作れない", emoji_cp="1f4e1", w=210, h=88)  # 📡

c.link(wow, core)
c.link(take, core)
c.link(only, core)

c.text(140, 236, "動かすと分かりやすい", scale="sm")
c.text(820, 236, "人に見せたくなる", scale="sm")

c.save("01-what-matters.svg")
