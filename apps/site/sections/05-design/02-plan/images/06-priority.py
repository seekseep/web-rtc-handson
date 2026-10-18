# 06-priority.svg
# スキーマ: NEAR-FAR + SOURCE-PATH-GOAL（目的に近いものから先に）
# 目的を「リリース」に絞ったので、収益化と解析が最後に回ったことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1080, 400)
c.text(540, 46, "目的に近いものから、先に", scale="xl")

goal = c.node(150, 200, "目的：\nリリース", emoji_cp="1f680", w=180, h=110)  # 🚀
first = c.node(420, 200, "遊べるゲーム\n申請の準備", shape="sticky", color="green", w=220, h=110)
then = c.node(690, 200, "効果音・振動\n地図・翻訳", shape="sticky", color="yellow", w=220, h=110)
last = c.node(950, 200, "広告\nアクセス解析", shape="sticky", color="gray", w=200, h=110)

c.link(goal, first)
c.link(first, then)
c.link(then, last)

c.text(420, 128, "まず", scale="md", fill=PALETTE["green"]["text"])
c.text(690, 128, "そのあと", scale="md", fill=PALETTE["yellow"]["text"])
c.text(950, 128, "最後に", scale="md", fill=PALETTE["gray"]["text"])

c.text(540, 350, "どれも大事。ただ、リリースできるかどうかに関わらないものは後ろに回す",
       scale="sm")

c.save("06-priority.svg")
