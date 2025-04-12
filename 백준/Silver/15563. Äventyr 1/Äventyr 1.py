import sys
g = lambda: map(int, sys.stdin.readline().split())
import bisect

N, Q = g()
input()
S = []
for _ in range(Q):
    c, v = g()
    if c == 1:
        if bisect.bisect_left(S, v) == bisect.bisect_right(S, v):
            bisect.insort(S, v)
    else:
        if not S:
            print(-1)
            continue
        i = bisect.bisect_left(S, v)
        n = float('inf')
        if i < len(S): n = min(n, S[i] - v)
        if i > 0: n = min(n, v - S[i - 1])
        print(n)