import sys
input = sys.stdin.readline

def period(t):
    if t <= 3: return 0
    if t <= 23: return 1
    if t <= 66: return 2
    if t <= 146: return 3
    if t <= 200: return 4
    if t <= 251: return 5
    if t <= 299: return 6
    if t <= 359: return 7
    if t <= 416: return 8
    if t <= 444: return 9
    if t <= 488: return 10
    if t <= 542: return 11
    return 12

def solve():
    for y in range(d):
        for x in range(w):
            ch = grid[y][x]
            if ch.isdigit():
                continue
            smin = 12
            for dy, dx in (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < d and 0 <= nx < w:
                    c2 = grid[ny][nx]
                    if '0' <= c2 <= '9':
                        smin = min(smin, ord(c2) - ord('0'))
            if ord(ch) - ord('A') != pt + smin:
                return "No"
    return "Yes"

for tc in range(1, int(input()) + 1):
    t, w, d = map(int, input().split())
    grid = [input() for _ in range(d)]
    pt = period(t)
    print(f"Data Set {tc}:\n{solve()}\n")