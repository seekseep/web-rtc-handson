# 00-thumbnail.svg
# スキーマ: NEAR-FAR（自分の丸は光るが、相手の丸は届かない）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "まずは、つなぐ前の画面をつくる", scale="xl")

c.ellipse(300, 150, 56, 56, color="yellow")
c.text(300, 232, "じぶん", scale="md")
c.ellipse(600, 150, 56, 56, color="gray")
c.text(600, 232, "あいて", scale="md")
c.connector(360, 150, 540, 150, dash="dashed", primary=False, label="まだ届かない", label_scale="sm")
c.text(450, 272, "ボタンを押すと、じぶんの丸だけが光る", scale="sm")

c.save("00-thumbnail.svg")
