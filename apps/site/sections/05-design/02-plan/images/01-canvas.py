# 02-canvas.svg
# スキーマ: CENTER-PERIPHERY（2 台が 1 枚のキャンバスを囲む）
# 勉強会の看板になるアプリの完成イメージ。2 台から同じ絵に描き込める

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 360)
c.text(480, 46, "2 台で、1 枚の絵を描く", scale="xl")

pc = c.node(150, 205, "PC", emoji_cp="1f4bb", w=180, h=100)  # 💻
art = c.node(480, 205, "同じキャンバス", emoji_cp="1f3a8", w=210, h=110)  # 🎨
phone = c.node(810, 205, "スマホ", emoji_cp="1f4f1", w=180, h=100)  # 📱

c.link(pc, art, label="描く")
c.link(phone, art, label="描く")

c.text(480, 336, "どちらが描いた線も、その場で両方の画面に出る", scale="sm")

c.save("02-canvas.svg")
