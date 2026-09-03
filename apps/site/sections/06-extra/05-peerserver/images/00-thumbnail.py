# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（頼み先を移す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 320)
c.text(450, 50, "ひと声の取り次ぎを、自分のサーバーに移す", scale="xl")

c.cloud(70, 108, 250, 120, color="gray")
c.text(195, 176, "PeerJS Cloud", scale="md", fill=PALETTE["gray"]["text"])
c.text(195, 254, "世界中の人と共有", scale="sm")

c.connector(346, 168, 508, 168, label="移す", label_scale="md", label_dy=-18)

c.node(710, 152, "自分の PeerServer", icon_name="server", label_scale="label")
c.text(710, 254, "名前がぶつかるのは自分のユーザーだけ", scale="sm")

c.save("00-thumbnail.svg")
