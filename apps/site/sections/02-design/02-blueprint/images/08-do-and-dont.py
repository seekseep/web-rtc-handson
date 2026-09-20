# 08-do-and-dont.svg
# スキーマ: CONTAINER × 2（やることの箱と、やらないことの箱）
# 「やらない」を決めるのも設計のうち、と分かるようにする

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(980, 330)
c.text(490, 44, "やることと、やらないことを分ける", scale="xl")

c.sticky(40, 78, 480, 190, color="green")
c.text(280, 110, "今日やる", scale="lg")
for cx, label, cp in [
    (140, "線", "270f"),  # ✏️
    (245, "色", "1f3a8"),  # 🎨
    (350, "けしごむ", "1f9fd"),  # 🧽
    (455, "ぜんぶ消す", "1f5d1"),  # 🗑️
]:
    c.node(cx, 190, label, emoji_cp=cp, w=96, h=76)

c.sticky(560, 78, 380, 190, color="gray")
c.text(750, 110, "今日はやらない", scale="lg")
for cx, label, cp in [
    (645, "保存", "1f4be"),  # 💾
    (750, "ログイン", "1f511"),  # 🔑
    (855, "3 人以上", "1f465"),  # 👥
]:
    c.node(cx, 190, label, emoji_cp=cp, w=96, h=76)

c.text(280, 300, "これだけで「いっしょにお絵かき」になる", scale="sm")
c.text(750, 300, "あとから足せる形にしておく", scale="sm")

c.save("08-do-and-dont.svg")
