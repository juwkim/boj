import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

N, M = map(int, input().split())
l = [Counter(input()) for _ in range(N)]
ans = 1e9
for i in range(1, N - 1):
    w = sum(M - l[k]['W'] for k in range(i))
    for j in range(i + 1, N):
        b = sum(M - l[k]['B'] for k in range(i, j))
        r = sum(M - l[k]['R'] for k in range(j, N))
        ans = min(ans, w + b + r)
print(ans)