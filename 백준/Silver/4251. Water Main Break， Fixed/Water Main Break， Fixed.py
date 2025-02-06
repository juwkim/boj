import sys
input = sys.stdin.readline
from math import dist

for tc in range(1, 1 + int(input())):
    n, v = input().split()
    n, v = int(n), float(v)
    nums = [[*map(float, input().split())] for _ in range(n)]
    visited = bytearray(n)
    ans = 1e9
    def solve(curx, cury, curt, water):
        global ans
        if water >= ans:
            return
        if all(visited):
            ans = min(ans, water)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                x, y, t, r = nums[i]
                nxtt = max(t, curt + dist((curx, cury), (x, y)) / v)
                solve(x, y, nxtt, water + r * max(0, nxtt - t))
                visited[i] = 0
    solve(0, 0, 0, 0)
    print(f"Data Set {tc}:\n{ans:.2f}\n")