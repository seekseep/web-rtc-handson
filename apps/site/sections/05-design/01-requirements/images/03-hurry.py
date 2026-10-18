# 03-hurry.svg
# スキーマ: COMPULSION（時間に押される）対 NEAR-FAR（いつでも離れられる）
# 時間制限があると真剣にやるしかなく、電車でやめどきを選べないことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1000, 420)
c.text(500, 46, "急かされると、やめどきを選べない", scale="xl")

c.sticky(40, 86, 440, 260, color="red")
c.text(260, 126, "時間に急かされる", scale="lg", fill=PALETTE["red"]["text"])
timer = c.node(150, 240, "持ち時間", emoji_cp="23f1", w=150, h=100)  # ⏱️
tense = c.node(370, 240, "真剣に\nやるしかない", shape="sticky", color="gray",
               w=170, h=96)
c.link(timer, tense)

c.sticky(520, 86, 440, 260, color="green")
c.text(740, 126, "急かされない", scale="lg", fill=PALETTE["green"]["text"])
train = c.node(630, 240, "電車で", emoji_cp="1f683", w=150, h=100)  # 🚃
stop = c.node(850, 240, "駅に着いたら\nやめられる", shape="sticky", color="gray",
              w=170, h=96)
c.link(train, stop)

c.text(500, 394, "電車で将棋のゲームをしていて感じたこと。遊べる人も場面も、急かされるほど限られる",
       scale="sm")

c.save("03-hurry.svg")
