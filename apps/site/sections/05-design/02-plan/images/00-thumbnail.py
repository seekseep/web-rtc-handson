# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（要件 → ルール → AI と作る → リリース）
# 節の入口。要件から出発して、リリースまでの道のりをたどることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(1000, 340)
c.text(500, 46, "要件から、リリースまで", scale="xl")

req = c.node(130, 180, "要件", shape="sticky", color="yellow", w=170, h=96)
rule = c.node(380, 180, "ルール", shape="hexagon", color="blue", w=180, h=110)
ai = c.node(630, 180, "AI と作る", emoji_cp="1f916", w=170, h=100)  # 🤖
ship = c.node(870, 180, "リリース", emoji_cp="1f680", w=170, h=100)  # 🚀

c.link(req, rule)
c.link(rule, ai)
c.link(ai, ship)

c.text(500, 316, "決めるのは人、作るのは AI。どの順で進めるかも、要件から決める", scale="sm")

c.save("00-thumbnail.svg")
