# 04-back.svg
# スキーマ: SPLITTING（表を引けたものだけ通す）+ FORCE:BLOCKAGE（引けないものは捨てる）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 420)
c.text(450, 48, "帰りの便は、表を逆に引いて配られる", scale="xl")

router = c.node(450, 175, "ルーター\nの表", shape="diamond", color="yellow", w=180, h=150)

replied = c.sticky(600, 86, 270, 92, color="green")
c.text(735, 118, "表に行があった", scale="sm", fill=PALETTE["green"]["text"])
c.text(735, 152, "203.0.113.42:60123 宛", scale="sm", font="technical")

stranger = c.sticky(600, 208, 270, 92, color="red")
c.text(735, 240, "表に行が無い", scale="sm", fill=PALETTE["red"]["text"])
c.text(735, 274, "いきなり来た通信", scale="sm")

pc = c.node(130, 175, "192.168.1.5", emoji_cp="1f4bb", color="blue", w=170, h=116)
trash = c.node(130, 320, "捨てる", emoji_cp="1f5d1", color="red", w=150, h=88)

c.link(replied, router)
c.link(router, pc, label="配れる", label_scale="sm")
c.link(stranger, router, primary=False)
c.link(router, trash, label="配れない", label_scale="sm", primary=False, dash="dashed")

c.text(
    500, 404, "外から声をかけられない理由は、悪意ではなく「行き先が分からない」から", scale="sm"
)

c.save("04-back.svg")
