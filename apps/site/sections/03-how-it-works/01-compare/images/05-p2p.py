# 05-p2p.svg
# スキーマ: LINK（直接つながる）+ 不在（真ん中に誰もいない）
# 自分と相手が、あいだに何も挟まずにつながっていることを見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 310)

c.text(480, 46, "今回作るのは、真ん中を通らないもの", scale="xl")

me = c.node(230, 165, "自分", emoji_cp="1f4bb")
you = c.node(730, 165, "相手", emoji_cp="1f4bb")

# 往路と復路に同じ offset を渡すと、互いに反対側の車線へ分かれる
c.link(me, you, label="こんにちは", label_scale="sm", offset=22)
c.link(you, me, primary=False, offset=22)

c.text(480, 256, "あいだに誰もいない", scale="md")
c.text(480, 284, "速いが、記録は残らない", scale="sm")

c.save("05-p2p.svg")
