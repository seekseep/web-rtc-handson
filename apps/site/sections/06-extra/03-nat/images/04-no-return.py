# 04-no-return.svg
# スキーマ: SOURCE-PATH-GOAL（行きは通る）+ FORCE:BLOCKAGE（帰りが行き先を持たない）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 440)
c.text(480, 48, "送り主の欄に書ける住所が無い", scale="xl")

me = c.node(170, 180, "自分  192.168.1.5", emoji_cp="1f4bb", w=160, h=88)
server = c.node(820, 180, "サーバー", emoji_cp="1f5c4")
lost = c.node(420, 340, "どこへ返す?", shape="diamond", color="red", w=230, h=124)

c.link(me, server, label="あて先は分かる", label_scale="sm", offset=24)
c.link(server, lost, label="送り主 192.168.1.5", label_scale="sm",
       primary=False, dash="dashed")

c.text(480, 424, "家の LAN の中だけの番号なので、外からは返せない", scale="sm")

c.save("04-no-return.svg")
