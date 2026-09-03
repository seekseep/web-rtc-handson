# 01-via-server.svg
# スキーマ: SOURCE-PATH-GOAL（人 → A → サーバー → B → 人）
# 両端に人を置き、話しているのは人であることを見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 292)

c.text(480, 46, "いつもの Web は、必ず真ん中を通る", scale="xl")

c.emoji("1f9d1", 62, 141, 56)
c.text(90, 217, "あなた", scale="label")
c.node(200, 165, "ブラウザ A", emoji_cp="1f310")

c.node(480, 165, "サーバー", emoji_cp="1f5a5")

c.node(760, 165, "ブラウザ B", emoji_cp="1f310")
c.emoji("1f9d1", 842, 141, 56)
c.text(870, 217, "相手", scale="label")

c.connector(250, 150, 430, 150, label="こんにちは", label_scale="sm")
c.connector(530, 150, 710, 150, label="こんにちは", label_scale="sm")

c.text(480, 266, "サーバーが預かって、配る。記録も残せる", scale="sm")

c.save("01-via-server.svg")
