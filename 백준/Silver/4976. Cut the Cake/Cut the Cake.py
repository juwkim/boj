import sys
input = sys.stdin.readline

def cut_piece(piece, s):
    x1, y1, x2, y2 = piece
    w, d = x2 - x1, y2 - y1
    perim = 2 * (w + d)
    s %= perim
    if s < w:
        cx = x1 + s
        return [(x1, y1, cx, y2), (cx, y1, x2, y2)]
    s -= w
    if s < d:
        cy = y1 + s
        return [(x1, y1, x2, cy), (x1, cy, x2, y2)]
    s -= d
    if s < w:
        cx = x2 - s
        return [(x1, y1, cx, y2), (cx, y1, x2, y2)]
    s -= w
    cy = y2 - s
    return [(x1, y1, x2, cy), (x1, cy, x2, y2)]

while True:
    n, w, d = map(int, input().split())
    if w == 0:
        break
    pieces = [(0, 0, w, d)]
    for _ in range(n):
        p, s = map(int, input().split())
        pieces.extend(sorted(cut_piece(pieces.pop(p - 1), s), key=lambda x: (x[0] - x[2]) * (x[1] - x[3])))
    print(*sorted((x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in pieces))