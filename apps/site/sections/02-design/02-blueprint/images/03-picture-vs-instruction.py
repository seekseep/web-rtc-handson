# 03-picture-vs-instruction.svg
# スキーマ: SOURCE-PATH-GOAL × 2 レーン（同じ区間を、重い荷と軽い荷が通る）
# 同じ「相手に届ける」でも、何を載せるかで通り道の太さが変わる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(920, 360)
c.text(460, 46, "同じ道を通すなら、軽いほうがいい", scale="xl")

pc_a = c.node(120, 128, "自分の PC", emoji_cp="1f4bb", w=140, h=88)  # 💻
sp_a = c.node(800, 128, "相手のスマホ", emoji_cp="1f4f1", w=140, h=88)  # 📱
c.link(pc_a, sp_a, label="キャンバスの画像まるごと", weight=9)
c.text(460, 196, "1 回で数万バイト。指を動かすたびに毎回", scale="sm")

pc_b = c.node(120, 268, "自分の PC", emoji_cp="1f4bb", w=140, h=88)  # 💻
sp_b = c.node(800, 268, "相手のスマホ", emoji_cp="1f4f1", w=140, h=88)  # 📱
c.link(pc_b, sp_b, label="「ここからここへ線を引いて」", weight=2)
c.text(460, 336, "1 回で数十バイト。届いた側が、自分で描く", scale="sm")

c.save("03-picture-vs-instruction.svg")
