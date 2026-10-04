# 02-layers.svg
# スキーマ: CONTAINER（入れ子）
# 自分はインターネットに直接ではなく、ISP の中の LAN の中にいる、を見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 460)
c.text(480, 48, "自分は、いちばん内側にいる", scale="xl")

c.sticky(60, 84, 840, 320, color="gray")
c.text(84, 120, "インターネット", scale="lg", align="left", fill=PALETTE["gray"]["text"])

c.sticky(132, 140, 696, 240, color="teal")
c.text(156, 176, "ISP", scale="lg", align="left", fill=PALETTE["teal"]["text"])

c.sticky(204, 196, 552, 160, color="blue")
c.text(228, 232, "家の LAN", scale="lg", align="left", fill=PALETTE["blue"]["text"])

c.node(480, 268, "自分  192.168.1.5", emoji_cp="1f4bb", w=150, h=88)

c.text(480, 438, "192.168.1.5 は、家の LAN の中だけで通じる番号", scale="sm")

c.save("02-layers.svg")
