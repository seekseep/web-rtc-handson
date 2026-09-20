# 05-p2p.svg
# スキーマ: LINK（直接つながる）+ 不在（真ん中に誰もいない）
# 両端に人を置き、人と人が直接つながっていることを見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 310)

c.text(480, 46, "今回作るのは、真ん中を通らないもの", scale="xl")

c.emoji("1f9d1", 92, 141, 56)
c.text(120, 217, "あなた", scale="label")
c.node(230, 165, "ブラウザ A", emoji_cp="1f310")

c.node(730, 165, "ブラウザ B", emoji_cp="1f310")
c.emoji("1f9d1", 812, 141, 56)
c.text(840, 217, "相手", scale="label")

c.connector(280, 132, 680, 132, label="こんにちは", label_scale="sm")
c.connector(680, 174, 280, 174, primary=False)

c.text(480, 256, "あいだに誰もいない", scale="md")
c.text(480, 284, "速いが、記録は残らない", scale="sm")

c.save("05-p2p.svg")
