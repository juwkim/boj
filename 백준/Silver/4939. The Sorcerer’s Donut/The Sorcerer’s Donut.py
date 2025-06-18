import sys
input = sys.stdin.readline
from collections import Counter

while True:
    h, w = map(int, input().split())
    if h == 0:
        break
    board = [input() for _ in range(h)]
    cnt = Counter()
    for x in range(h):
        for y in range(w):
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                path = []
                visited = set()
                cx, cy = x, y
                for length in range(1, h * w + 1):
                    if (cx, cy) in visited:
                        break
                    path.append(board[cx][cy])
                    visited.add((cx, cy))
                    if length >= 2:
                        cnt[''.join(path)] += 1
                    cx = (cx + dx) % h
                    cy = (cy + dy) % w
    best, bestlen = '0', 0
    for k, v in cnt.items():
        if v >= 2 and (len(k) > bestlen or (len(k) == bestlen and k < best)):
            best, bestlen = k, len(k)
    print(best)