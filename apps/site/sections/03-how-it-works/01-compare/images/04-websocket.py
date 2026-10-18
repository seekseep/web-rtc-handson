# 04-websocket.svg
# スキーマ: SOURCE-PATH-GOAL（自分 → サーバー → 相手 の中継）+ LINK（つなぎっぱなしの線）
# 「同じ言葉が 2 回運ばれる」ことでサーバーが配り手だと分かるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 384)
c.text(480, 46, "WebSocket で、つなぎっぱなしにする", scale="xl")

me = c.node(140, 180, "自分", emoji_cp="1f4bb")
server = c.node(480, 180, "サーバー", emoji_cp="1f5c4")
you = c.node(820, 180, "相手", emoji_cp="1f4bb")

# 上の車線が「運ばれる言葉」、下の車線が「切れない接続」
c.link(me, server, label="こんにちは", label_scale="sm", offset=24)
c.link(server, you, label="こんにちは", label_scale="sm", offset=24)
c.link(me, server, both=True, primary=False, offset=-24)
c.link(server, you, both=True, primary=False, offset=-24)
c.text(310, 230, "つなぎっぱなし", scale="sm")
c.text(650, 230, "つなぎっぱなし", scale="sm")

c.text(480, 292, "サーバーが受け取って、配る。だからサーバーからも送れる", scale="sm")

c.raw('<line x1="200" y1="330" x2="760" y2="330" stroke="#cbd5e1" '
      'stroke-width="2" stroke-dasharray="7 6"/>')
c.emoji("274c", 462, 312, 36)
c.text(480, 372, "リアルタイムだけれど、自分と相手は直接つながっていない", scale="sm")

c.save("04-websocket.svg")
