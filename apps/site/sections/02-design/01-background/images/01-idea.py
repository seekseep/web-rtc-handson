# 01-idea.svg
# スキーマ: SOURCE-PATH-GOAL（目的と制約 → アイデア → 技術候補）
# 技術の優劣を比べる図ではなく、アイデアが生まれる流れを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(1020, 400)
c.text(510, 46, "条件から、アイデア、そして技術候補へ", scale="xl")

goal = c.node(150, 155, "作る楽しさ", emoji_cp="1f389", w=180, h=88)  # 🎉
limit = c.node(150, 285, "4 時間弱・1〜3 年目", emoji_cp="23f0", w=240, h=88)  # ⏰
idea = c.node(500, 220, "いっしょに動かす", emoji_cp="1f4a1", w=210, h=96)  # 💡
tech = c.node(850, 220, "WebRTC", emoji_cp="1f4e1", w=190, h=96)  # 📡

c.link(goal, idea, label="目的")
c.link(limit, idea, label="制約")
c.link(idea, tech, label="できそう？")

c.text(510, 380, "ここで決まるのは「使う技術」まで。作るものはまだ決まっていない", scale="sm")

c.save("01-idea.svg")
