# 02-priority.svg
# スキーマ: CENTER-PERIPHERY（中心に置く体験と、その外側に回すもの）
# 3 時間で全部はできないので、何を中心に据えるかを決めたことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(980, 440)
c.text(490, 46, "中心に置くものを、1 つに決める", scale="xl")

core = c.node(490, 230, "リアルタイム通信\nを体験する", shape="ellipse",
              color="blue", w=290, h=150)

catchy = c.node(180, 150, "見せたくなる", emoji_cp="1f3a8", w=200, h=96)  # 🎨
extend = c.node(180, 330, "自分で広げる", emoji_cp="1f6e0", w=200, h=96)  # 🛠️
later = c.node(840, 230, "発展させる", shape="sticky", color="gray",
               w=210, h=96)

c.link(catchy, core, primary=False)
c.link(extend, core, primary=False)
c.link(core, later, dash="dashed", primary=False, label="動いたあとで")

c.text(490, 414, "全部を作り込まない。まず中心の体験を成立させて、そこから広げる", scale="sm")

c.save("02-priority.svg")
