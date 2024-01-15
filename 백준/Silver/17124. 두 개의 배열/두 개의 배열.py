import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect_left

for _ in range(int(input())):
    n, m = g()
    A = g()
    B = sorted(g())
    ans = 0
    for a in A:
        idx = bisect_left(B, a)
        if idx == 0:
            ans += B[0]
        elif idx == m:
            ans += B[m - 1]
        else:
            ans += min([B[idx-1], B[idx]], key=lambda x: abs(x - a))
    print(ans)