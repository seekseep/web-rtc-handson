# 03-stun.svg
# スキーマ: CYCLE（聞きに行って、答えが返る）+ CONTAINER（LAN の中 / 外）
# 行きの途中でルーターが送り主を書き換え、STUN はそれを読み上げて返すだけ、を見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 380)
c.text(480, 48, "STUN は、届いた送り主を読み上げるだけ", scale="xl")

# ルーターは枠のすぐ外に置く。枠の上に載せると、下の文字に枠線がかぶる
c.sticky(40, 84, 380, 212, color="gray")
c.text(64, 116, "LAN", scale="lg", align="left", fill=PALETTE["gray"]["text"])

pc = c.node(170, 196, "自分", emoji_cp="1f4bb")
router = c.node(500, 196, "ルーター", emoji_cp="1f4f6")
stun = c.node(820, 196, "STUN サーバー", emoji_cp="1f5c4")

# 上の車線が行き（送り主が書き換わる）、下の車線が返事
c.link(pc, router, label="送り主 192.168.1.10", label_scale="sm", offset=24)
c.link(router, stun, label="送り主 203.0.113.10", label_scale="sm", offset=24)
c.link(stun, router, label="203.0.113.10 から来たよ", label_scale="sm",
       label_fill=PALETTE["blue"]["text"], primary=False, offset=24)
c.link(router, pc, primary=False, offset=24)

c.text(500, 272, "ここで書き換わる", scale="sm", fill=PALETTE["gray"]["text"])

c.text(480, 336, "自分では分からない外の住所を、外から教えてもらう", scale="md")
c.text(480, 362, "教わった住所が srflx 候補になる。STUN は通信を運ばない", scale="sm")

c.save("03-stun.svg")
