# 02-switch.svg
# スキーマ: SOURCE-PATH-GOAL × 4 コマ（ふさがれる → スイッチを通す → 開く → つながる）
# スイッチは「つなぐ順番」を考えさせる仕掛けだと、1 枚の盤面の移り変わりで見せる
# 盤面は頂点が上の六角形 2 段。上の段が赤、下の段が青。◆ のスイッチは赤の通り道、◆ の壁は青の通り道にある

import math
import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE, INK_SCALE

c = Canvas(1340, 450)
c.text(670, 46, "つなぐ順番で、壁が開く", scale="xl")

S = 28                      # 六角形の半径（中心から頂点まで）
CW = math.sqrt(3) * S       # 1 マスの幅
ROW = 1.5 * S               # 段の間隔
N = 5                       # 1 段のマス数
RED = PALETTE["red"]["border"]
BLUE = PALETTE["blue"]["border"]
WALL = PALETTE["purple"]["border"]
CELL_FILL = "#ffffff"
CELL_LINE = INK_SCALE["gray"]


def center(x0, y0, row, i):
    """row 0 = 上の段（赤）、row 1 = 下の段（青、半マス右にずれる）。"""
    return (x0 + i * CW + (CW / 2 if row else 0), y0 + row * ROW)


def hexagon(cx, cy):
    pts = [(cx + S * math.cos(math.radians(a)), cy + S * math.sin(math.radians(a)))
           for a in (-90, -30, 30, 90, 150, 210)]
    points = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    c.raw(f'<polygon points="{points}" fill="{CELL_FILL}" stroke="{CELL_LINE}" stroke-width="1.5"/>')


def diamond(cx, cy, r, fill):
    c.raw(f'<polygon points="{cx:.1f},{cy - r:.1f} {cx + r:.1f},{cy:.1f} '
          f'{cx:.1f},{cy + r:.1f} {cx - r:.1f},{cy:.1f}" fill="{fill}"/>')


def path(points, color):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    c.raw(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="10" '
          f'stroke-linecap="round" stroke-linejoin="round" opacity="0.85"/>')


def dot(cx, cy, color):
    c.raw(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="11" fill="{color}"/>')


def panel(x, step, text, red_drawn, wall_open, blue_cells):
    w, h = 300, 270
    c.sticky(x, 86, w, h, color="gray", weight="thin")
    c.text(x + 28, 122, str(step), scale="lg", align="left", fill=PALETTE["blue"]["text"])

    x0 = x + (w - (N * CW + CW / 2)) / 2 + CW / 2
    y0 = 200
    for row in (0, 1):
        for i in range(N):
            hexagon(*center(x0, y0, row, i))

    # 線（点より先に描いて、点を上に重ねる）
    if red_drawn:
        path([center(x0, y0, 0, i) for i in range(N)], RED)
    if blue_cells:
        path([center(x0, y0, 1, i) for i in blue_cells], BLUE)

    # ◆ の壁（下の段の 2 つめと 3 つめの間の辺）
    ex = center(x0, y0, 1, 1)[0] + CW / 2
    ey = y0 + ROW
    if wall_open:
        c.raw(f'<line x1="{ex:.1f}" y1="{ey - S / 2:.1f}" x2="{ex:.1f}" y2="{ey + S / 2:.1f}" '
              f'stroke="{WALL}" stroke-width="3" stroke-dasharray="4 4" opacity="0.6"/>')
    else:
        c.raw(f'<line x1="{ex:.1f}" y1="{ey - S / 2 - 2:.1f}" x2="{ex:.1f}" y2="{ey + S / 2 + 2:.1f}" '
              f'stroke="{WALL}" stroke-width="8" stroke-linecap="round"/>')
    diamond(ex, ey + S / 2 + 16, 6, WALL)

    # ◆ のスイッチ（上の段のまん中）。線の上に重ねて、通っていることが見えるようにする
    sx, sy = center(x0, y0, 0, 2)
    c.raw(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="12" fill="#ffffff" stroke="{WALL}" stroke-width="2"/>')
    diamond(sx, sy, 7, WALL)

    for i in (0, N - 1):
        dot(*center(x0, y0, 0, i), RED)
        dot(*center(x0, y0, 1, i), BLUE)

    c.text(x + w / 2, 318, text, scale="md")


panel(40, 1, "青は ◆ の壁で\n通れない", red_drawn=False, wall_open=False, blue_cells=[0, 1])
panel(360, 2, "先に赤をつなぐ。\n赤は ◆ のスイッチを通る", red_drawn=True, wall_open=False, blue_cells=[0, 1])
panel(680, 3, "赤がつながると、\n◆ の壁が開く", red_drawn=True, wall_open=True, blue_cells=[0, 1])
panel(1000, 4, "青も通れるように\nなって、つながる", red_drawn=True, wall_open=True, blue_cells=[0, 1, 2, 3, 4])

c.text(670, 410, "どの色を先につなぐかを考えるパズルになる。時間に急かされずに、じっくり考えられる", scale="sm")

c.save("02-switch.svg")
