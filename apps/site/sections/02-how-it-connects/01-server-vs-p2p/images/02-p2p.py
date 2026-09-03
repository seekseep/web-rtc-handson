# 02-p2p.svg
# スキーマ: LINK（直接つながる）+ 不在（真ん中に誰もいない）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)

c.text(450, 46, "今回作るのは、真ん中を通らないもの", scale="xl")
c.node(200, 165, "ブラウザ A", emoji_cp="1f310")
c.node(700, 165, "ブラウザ B", emoji_cp="1f310")
c.connector(268, 140, 632, 140, label="こんにちは", label_scale="sm")
c.connector(632, 190, 268, 190, primary=False)
c.text(450, 254, "あいだに誰もいない", scale="md")
c.text(450, 282, "速いが、記録は残らない", scale="sm")

c.save("02-p2p.svg")
