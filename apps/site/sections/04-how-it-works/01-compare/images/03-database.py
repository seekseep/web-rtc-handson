# 03-database.svg
# スキーマ: SOURCE-PATH-GOAL（相手 → サーバー/DB）+ BLOCKAGE（自分へは勝手に届かない）
# 「保存はされている。ただし自分の画面は、こちらから取りに行くまで変わらない」を見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 440)
c.text(480, 48, "③ DB に入れれば、他人の変更も残る", scale="xl")

other = c.node(170, 140, "相手のブラウザ", emoji_cp="1f310")
store = c.node(760, 230, "サーバー + DB", shape="cylinder", color="green",
               w=200, h=130)
me = c.node(170, 340, "自分のブラウザ", emoji_cp="1f310")

c.link(other, store, label="書きこむ")

# 往路と復路に同じ offset を渡すと、互いに反対側の車線へ分かれる
c.link(me, store, label="リロードして、取りに行く", offset=36)
c.link(store, me, offset=36, primary=False, dash="dashed", head=False)
c.emoji("274c", 448, 296, 30)
c.text(465, 356, "サーバーの側から知らせてはくれない", scale="sm")

c.text(480, 416,
       "相手が書いた瞬間には、自分の画面は変わらない。"
       "次にこちらから聞いたときに、はじめて見える", scale="sm")

c.save("03-database.svg")
