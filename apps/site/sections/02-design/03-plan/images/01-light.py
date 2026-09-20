# 01-light.svg
# スキーマ: SOURCE-PATH-GOAL（操作 → データ送信 → 相手の画面が変わる）
# 最初に作るいちばん小さいアプリ。通信できたことが目で見てわかる形にする

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 340)
c.text(480, 46, "押したことが、相手の画面に出る", scale="xl")

press = c.node(150, 195, "ボタンを押す", emoji_cp="1f4bb", w=190, h=96)  # 💻
send = c.node(480, 195, "色を送る", emoji_cp="1f4e1", w=170, h=96)  # 📡
light = c.node(810, 195, "丸が光る", emoji_cp="1f4f1", w=170, h=96)  # 📱

c.link(press, send)
c.link(send, light)

c.text(480, 316, "操作したことが、そのまま相手の画面の変化になる", scale="sm")

c.save("01-light.svg")
