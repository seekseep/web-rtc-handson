# 04-websocket.svg
# スキーマ: SOURCE-PATH-GOAL（A → サーバー → B の中継）+ LINK（つなぎっぱなしの線）
# 「同じ言葉が 2 回運ばれる」ことでサーバーが配り手だと分かるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 384)
c.text(480, 46, "③ WebSocket で、つなぎっぱなしにする", scale="xl")

c.node(140, 180, "ブラウザ A", emoji_cp="1f310")
c.node(480, 180, "サーバー", emoji_cp="1f5a5")
c.node(820, 180, "ブラウザ B", emoji_cp="1f310")

c.connector(196, 150, 428, 150, label="こんにちは", label_scale="sm")
c.connector(532, 150, 764, 150, label="こんにちは", label_scale="sm")
c.biconnector(196, 198, 428, 198, primary=False)
c.biconnector(532, 198, 764, 198, primary=False)
c.text(312, 226, "つなぎっぱなし", scale="sm")
c.text(648, 226, "つなぎっぱなし", scale="sm")

c.text(480, 292, "サーバーが受け取って、配る。だからサーバーからも送れる", scale="sm")

c.raw('<line x1="200" y1="330" x2="760" y2="330" stroke="#cbd5e1" '
      'stroke-width="2" stroke-dasharray="7 6"/>')
c.emoji("274c", 462, 312, 36)
c.text(480, 372, "リアルタイムだけれど、A と B は直接つながっていない", scale="sm")

c.save("04-websocket.svg")
