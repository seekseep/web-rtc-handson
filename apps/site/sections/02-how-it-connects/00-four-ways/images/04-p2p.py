# 04-p2p.svg
# スキーマ: LINK（A と B の直接の線）+ NEAR-FAR（サーバーは上に遠ざける）
# ③ との違いは「線が真ん中を通らない」こと。サーバーは破線で、つながるまでだけ

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 384)
c.text(480, 46, "④ ブラウザ同士を、直接つなぐ", scale="xl")

c.node(480, 118, "シグナリングサーバー", emoji_cp="1f5a5")
c.node(140, 262, "ブラウザ A", emoji_cp="1f310")
c.node(820, 262, "ブラウザ B", emoji_cp="1f310")

c.connector(190, 222, 432, 118, dash="dashed", primary=False,
            label="つながるまでだけ", label_scale="sm", label_dy=-14)
c.connector(528, 118, 770, 222, dash="dashed", primary=False)

c.biconnector(200, 262, 760, 262, primary=True, weight="thin")
c.text(480, 244, "こんにちは（直接）", scale="label")

c.text(480, 360, "つながったあとは、サーバーを通らない", scale="sm")

c.save("04-p2p.svg")
