import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect, insort

N, Q = g()
input()
S = [-1e9, 1e9]
for _ in range(Q):
    c, v = g()
    if c == 1:
        insort(S, v)
    elif len(S) == 2:
        print(-1)
    else:
        i = bisect(S, v)
        print(min(S[i] - v, v - S[i - 1]))