# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（ふわっとした相談が、作れそうなものに変わるまで）
# 要望は「使う技術」までしか決めてくれない、という章の入口を見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 300)
c.text(480, 46, "話から、作れそうなものへ", scale="xl")

talk = c.node(130, 160, "相談", emoji_cp="1f4ac", w=140, h=88)  # 💬
tech = c.node(410, 160, "リアルタイム通信", emoji_cp="1f4e1", w=170, h=88)  # 📡
spike = c.node(690, 160, "小さく試す", emoji_cp="1f52c", w=150, h=88)  # 🔬
ok = c.node(890, 160, "できそう", emoji_cp="2705", w=110, h=88)  # ✅

c.link(talk, tech, label="何を作る？")
c.link(tech, spike)
c.link(spike, ok)

c.text(480, 268, "ここまでで決まるのは「使う技術」まで。作るものはまだ決まっていない", scale="sm")

c.save("00-thumbnail.svg")
