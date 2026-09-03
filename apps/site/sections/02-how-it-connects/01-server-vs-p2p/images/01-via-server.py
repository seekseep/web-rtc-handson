# 01-via-server.svg
# スキーマ: SOURCE-PATH-GOAL（A → サーバー → B）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)

c.text(450, 46, "いつもの Web は、必ず真ん中を通る", scale="xl")
c.node(140, 165, "ブラウザ A", emoji_cp="1f310")
c.node(450, 165, "サーバー", emoji_cp="1f5a5")
c.node(760, 165, "ブラウザ B", emoji_cp="1f310")
c.connector(206, 150, 384, 150, label="こんにちは", label_scale="sm")
c.connector(516, 150, 694, 150, label="こんにちは", label_scale="sm")
c.text(450, 272, "サーバーが預かって、配る。記録も残せる", scale="sm")

c.save("01-via-server.svg")
