import sys
input = sys.stdin.readline
from itertools import permutations

def chebyshev_time(x1, y1, x2, y2, is_not_first_move):
    move_time = 100 * max(abs(x1 - x2), abs(y1 - y2))
    if is_not_first_move:
        return max(750, move_time)
    return move_time

for tc in range(1, int(input()) + 1):
    Z = int(input())
    xs, ys, ms = zip(*[[*map(int, input().split())] for _ in range(Z)])
    ans = 0
    visited = bytearray(Z)
    def solve(x, y, t, cnt):
        global ans
        ans = max(ans, cnt)
        for i in range(Z):
            if visited[i]:
                continue
            nxt_time = max(ms[i], t + chebyshev_time(x, y, xs[i], ys[i], cnt))
            if nxt_time <= ms[i] + 1000:
                visited[i] = 1
                solve(xs[i], ys[i], nxt_time, cnt + 1)
                visited[i] = 0
    solve(0, 0, 0, 0)
    print(f"Case #{tc}: {ans}")