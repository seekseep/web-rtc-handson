# 00-thumbnail.svg
# スキーマ: CONTAINER（app/ の中に 3 ファイル）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "エディタと作業フォルダを用意する", scale="xl")

editor = c.node(200, 165, "エディタ", emoji_cp="1f9d1-200d-1f4bb")
folder = c.sticky(400, 96, 440, 150, color="yellow")
c.emoji("1f4c1", 428, 112, 36)
c.text(478, 138, "app/", scale="lg", align="left", fill=PALETTE["yellow"]["text"], font="technical")
c.text(428, 180, "index.html", scale="sm", align="left", font="technical")
c.text(428, 206, "style.css", scale="sm", align="left", font="technical")
c.text(428, 232, "main.js", scale="sm", align="left", font="technical")
c.link(editor, folder, label="ここを開く", label_scale="sm", start="e", end="w")

c.save("00-thumbnail.svg")
