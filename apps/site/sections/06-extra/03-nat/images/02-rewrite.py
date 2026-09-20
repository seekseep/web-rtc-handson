# 02-rewrite.svg
# スキーマ: SOURCE-PATH-GOAL（荷物が通る）+ CONTACT（通過点で送り主の欄が書き換わる）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 340)
c.text(450, 48, "書き換わるのは「送り主」の欄だけ", scale="xl")

before = c.sticky(40, 90, 290, 130, color="blue")
c.text(185, 122, "家の中を出るとき", scale="sm", fill=PALETTE["blue"]["text"])
c.text(185, 158, "送り主 192.168.1.5:51000", scale="sm", font="technical")
c.text(185, 192, "あて先 93.184.216.34:443", scale="sm", font="technical")

router = c.node(450, 155, "ルーター", emoji_cp="1f4e1", color="yellow", w=130, h=110)

after = c.sticky(570, 90, 290, 130, color="orange")
c.text(715, 122, "外へ出たあと", scale="sm", fill=PALETTE["orange"]["text"])
c.text(715, 158, "送り主 203.0.113.42:60123", scale="sm", font="technical")
c.text(715, 192, "あて先 93.184.216.34:443", scale="sm", font="technical")

c.link(before, router)
c.link(router, after)

c.text(450, 282, "あて先はそのまま。IP だけでなくポート番号も付け替える", scale="sm")
c.text(450, 312, "だから 1 つの住所を、家じゅうの機器で分け合える", scale="sm")

c.save("02-rewrite.svg")
