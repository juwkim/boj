import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect, insort

N, Q = g()
input()
S = [-1e9, 1e9]
for _ in range(Q):
    c, v = g()
    i = bisect(S, v)
    if c == 1:
        if i == 0 or S[i - 1] != v:
            insort(S, v)
    elif len(S) == 2:
        print(-1)
    else:
        print(min(S[i] - v, v - S[i - 1]))