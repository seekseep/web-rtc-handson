# 01-who-decides.svg
# スキーマ: SPLITTING（色を送る場合 / 送らない場合）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "色を指示に入れるかどうかで、結果が変わる", scale="xl")
c.sticky(50, 84, 380, 250, color="green")
c.text(240, 116, "色を送る（正しい）", scale="lg", fill=PALETTE["green"]["text"])
c.text(240, 150, "{ ..., color: '#e5484d' }", scale="sm", font="technical")
c.raw('<rect x="80" y="176" width="140" height="90" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M100 250 Q 150 190 200 210" fill="none" stroke="#e5484d" stroke-width="7" stroke-linecap="round"/>')
c.raw('<rect x="260" y="176" width="140" height="90" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M280 250 Q 330 190 380 210" fill="none" stroke="#e5484d" stroke-width="7" stroke-linecap="round"/>')
c.text(240, 300, "両方の画面が同じ絵になる", scale="sm")
c.sticky(470, 84, 380, 250, color="red")
c.text(660, 116, "色を送らない（ズレる）", scale="lg", fill=PALETTE["red"]["text"])
c.text(660, 150, "{ ... }  ← 受け取った側の色を使う", scale="sm", font="technical")
c.raw('<rect x="500" y="176" width="140" height="90" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M520 250 Q 570 190 620 210" fill="none" stroke="#e5484d" stroke-width="7" stroke-linecap="round"/>')
c.raw('<rect x="680" y="176" width="140" height="90" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M700 250 Q 750 190 800 210" fill="none" stroke="#006fee" stroke-width="7" stroke-linecap="round"/>')
c.text(660, 300, "同じ絵を見ているつもりで、違うものを見ている", scale="sm")
c.text(450, 366, "絵に残るものは指示に入れる。手元の状態（選択中の道具）は送らない", scale="sm")

c.save("01-who-decides.svg")
