# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（2 つの条件が、1 つの問いに合流する）
# 章の入口。決まっているのは「体験してほしいこと」と「時間・対象」だけだと見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(840, 390)
c.text(420, 46, "何を作ろう？", scale="xl")

fun = c.node(160, 150, "作る楽しさ", emoji_cp="1f389", w=180, h=88)  # 🎉
limit = c.node(160, 280, "4 時間弱", emoji_cp="23f0", w=180, h=88)  # ⏰
ask = c.node(610, 215, "題材を決める", emoji_cp="1f4ac", w=190, h=96)  # 💬

c.link(fun, ask, label="体験してほしいこと")
c.link(limit, ask, label="守る条件")

c.text(420, 370, "決まっているのは条件だけ。作るものは、これから決める", scale="sm")

c.save("00-thumbnail.svg")
