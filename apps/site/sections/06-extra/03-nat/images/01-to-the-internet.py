# 01-to-the-internet.svg
# スキーマ: SOURCE-PATH-GOAL（端末から外の世界まで、機械を順に通る）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 300)
c.text(480, 48, "端末からインターネットまでに通るもの", scale="xl")

pc = c.node(100, 150, "PC・スマホ", emoji_cp="1f4bb", w=150, h=110)
router = c.node(310, 150, "ルーター", emoji_cp="1f4e1", color="yellow", w=150, h=110)
onu = c.node(520, 150, "ONU・モデム", emoji_cp="1f50c", color="gray", w=150, h=110)
isp = c.node(730, 150, "ISP", emoji_cp="1f3e2", color="teal", w=140, h=110)
net = c.node(900, 150, "世界", shape="cloud", color="gray", w=130, h=104)

c.link(pc, router)
c.link(router, onu)
c.link(onu, isp)
c.link(isp, net)

c.text(310, 246, "ここで住所を書き換える", scale="sm")
c.text(730, 246, "グローバル住所を貸す", scale="sm")

c.text(480, 284, "住所が書き換わるのはルーターの 1 か所だけ", scale="sm")

c.save("01-to-the-internet.svg")
