# 03-relay.svg
# スキーマ: SOURCE-PATH-GOAL（A → サーバー → B）+ 代償の列挙
# 同じ 1 通が 2 回運ばれること、その代金がサーバー側に乗ることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 340)

c.text(480, 48, "真ん中を通すと、同じ 1 通が 2 回運ばれる", scale="xl")

a = c.node(150, 150, "ブラウザ A", emoji_cp="1f310")
sv = c.node(480, 150, "サーバー", emoji_cp="1f5a5")
b = c.node(810, 150, "ブラウザ B", emoji_cp="1f310")

c.link(a, sv, label="こんにちは", label_scale="sm")
c.link(sv, b, label="こんにちは", label_scale="sm")

costs = [
    (250, "23f0", "遅くなる"),
    (480, "1f4c8", "混む"),
    (710, "1f4b0", "お金がかかる"),
]
for cx, cp, name in costs:
    c.emoji(cp, cx - 17, 240, 34)
    c.text(cx, 296, name, scale="md")

c.text(480, 326, "運んだ量のぶんだけ、サーバーの側に負担と料金が乗る", scale="sm")

c.save("03-relay.svg")
