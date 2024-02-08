import sys
input = sys.stdin.readline
from math import inf

n, m = map(int, input().split())
milk = [int(input()) for _ in range(m)]
if sum(milk) < n:
    print("IMPOSSIBLE")
else:
    ans = inf
    def solve(idx, num):
        global ans
        if idx == m:
            if num >= n:
                ans = min(ans, num)
            return
        solve(idx + 1, num)
        solve(idx + 1, num + milk[idx])
    solve(0, 0)
    print(ans)