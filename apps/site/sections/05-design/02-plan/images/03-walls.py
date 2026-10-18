# 03-walls.svg
# スキーマ: BLOCKAGE（通れない場所をどこに置くか）
# 通れないマスは見た目もルールも増えるが、マスの間の壁ならどちらも変わらないことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1000, 440)
c.text(500, 46, "「通れない」を、どこに置くか", scale="xl")

W, H = 84, 72  # 六角形 1 マス（平らな辺が上）
STEP = W * 0.78  # genfig の六角形は左右の斜辺が幅の 0.22。この間隔で辺がぴったり重なる


def blocked_cell(x, y):
    """通れないマス。黒く塗りつぶし、白い ✕ を重ねる。"""
    d = W * 0.22
    pts = [(x + d, y), (x + W - d, y), (x + W, y + H / 2),
           (x + W - d, y + H), (x + d, y + H), (x, y + H / 2)]
    points = " ".join(f"{px:g},{py:g}" for px, py in pts)
    c.raw(f'<polygon points="{points}" fill="#1e293b" stroke="#1e293b" '
          f'stroke-width="3.5" stroke-linejoin="round"/>')
    cx, cy, r = x + W / 2, y + H / 2, 15
    for sx in (1, -1):
        c.raw(f'<line x1="{cx - r:g}" y1="{cy - sx * r:g}" x2="{cx + r:g}" y2="{cy + sx * r:g}" '
              f'stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>')


def row(x0, y, blocked=None):
    for i in range(4):
        x, yy = x0 + i * STEP, y + (H / 2 if i % 2 else 0)
        if i == blocked:
            blocked_cell(x, yy)
        else:
            c.hexagon(x, yy, W, H, color="blue")


c.sticky(40, 86, 440, 280, color="red", weight="thin")
c.text(260, 126, "通れないマス", scale="lg", fill=PALETTE["red"]["text"])
row(122, 160, blocked=2)
c.text(260, 318, "見た目が 1 種類増える", scale="md")
c.text(260, 346, "「全マスで ★」が言い直しになる", scale="md")

c.sticky(520, 86, 440, 280, color="green", weight="thin")
c.text(740, 126, "マスの間の壁", scale="lg", fill=PALETTE["green"]["text"])
row(602, 160)
# 2 つめ（下段）と 3 つめ（上段）のマスが共有する斜めの辺に、壁を太線で引く
x1 = 602 + STEP
c.raw(f'<line x1="{x1 + STEP:g}" y1="{160 + H / 2:g}" x2="{x1 + W:g}" y2="{160 + H:g}" '
      f'stroke="{PALETTE["red"]["border"]}" stroke-width="9" stroke-linecap="round"/>')
c.text(740, 318, "マスはどれも同じ見た目", scale="md")
c.text(740, 346, "「全マスで ★」はそのまま", scale="md")

c.text(500, 410, "同じ「通れない」でも、置く場所で増えるものが変わる", scale="sm")

c.save("03-walls.svg")
