# 03-nat.svg
# スキーマ: CONTAINER（家の中）+ BLOCKAGE（外からはローカル住所に届かない）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "外から見えるのは、ルーターの住所ひとつだけ", scale="xl")
c.sticky(50, 84, 380, 240, color="yellow")
c.text(240, 116, "家の中", scale="lg", fill=PALETTE["yellow"]["text"])
c.emoji("1f4bb", 100, 140, 46)
c.text(190, 170, "192.168.1.5", scale="sm", align="left", font="technical")
c.emoji("1f4f1", 100, 210, 46)
c.text(190, 240, "192.168.1.8", scale="sm", align="left", font="technical")
c.emoji("1f4e1", 100, 272, 46)
c.text(190, 302, "ルーター（NAT）", scale="sm", align="left")
c.node(720, 200, "インターネット", emoji_cp="1f30d", w=180, h=100)
c.text(720, 268, "203.0.113.42", scale="sm", font="technical")
c.text(720, 292, "外から見えるのはこれだけ", scale="sm")
c.connector(440, 210, 640, 210, primary=False)
c.connector(640, 260, 440, 260, dash="dashed", primary=False, label="192.168.1.5 宛は届かない", label_scale="sm")
c.text(450, 356, "自分の「外から見た住所」を、自分では知らない", scale="sm")

c.save("03-nat.svg")
