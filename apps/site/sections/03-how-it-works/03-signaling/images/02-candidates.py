# 02-candidates.svg
# スキーマ: CONTAINER（LAN の中 / 外）+ NEAR-FAR（内側の住所ほど通じる相手が狭い）
# 同じパソコンに住所が 3 つあり、それぞれ通じる相手が違うことを見せる。
# 色はデモの候補タグ（host 灰 / srflx 青 / relay 紫）にそろえる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 420)
c.text(480, 48, "1 台のパソコンに、住所が 3 つある", scale="xl")

# ルーターは枠のすぐ外に置く。枠の上に載せると、ルーターの下の住所に枠線が
# かぶって読めない。枠は LAN（デモの囲みと同じ呼び方）にして、境目にいることを見せる
c.sticky(40, 84, 420, 250, color="gray")
c.text(64, 116, "LAN", scale="lg", align="left", fill=PALETTE["gray"]["text"])

pc = c.node(190, 184, "自分", emoji_cp="1f4bb")
router = c.node(540, 184, "ルーター", emoji_cp="1f4f6")
turn = c.node(820, 184, "TURN サーバー", emoji_cp="1f5c4")
c.link(pc, router, primary=False)
c.link(router, turn, primary=False, dash="dashed")

cols = [
    (190, "gray", "host", "192.168.1.10", "LAN の中の住所", "同じ LAN の相手だけ"),
    (540, "blue", "srflx", "203.0.113.10", "外から見た住所", "たいていの相手"),
    (820, "purple", "relay", "192.0.2.50", "TURN に借りた住所", "ほぼ誰とでも（中継）"),
]
for x, color, kind, addr, what, reach in cols:
    c.text(x, 266, kind, scale="md", fill=PALETTE[color]["text"], font="technical")
    c.text(x, 292, addr, scale="sm", font="technical")
    c.text(x, 316, what, scale="sm")
    c.text(x, 372, reach, scale="md", fill=PALETTE[color]["text"])

c.text(480, 404, "どれが相手に通じるかは、試してみるまで分からない", scale="sm")

c.save("02-candidates.svg")
