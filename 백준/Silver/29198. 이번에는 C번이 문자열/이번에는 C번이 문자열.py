import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N, M, K = g()
A = sum(map(Counter, sorted(sorted(input()) for _ in range(N))[:K]), Counter())
ans = []
for k, v in sorted(A.items()):
    ans.extend([k] * v)
print(*ans, sep='')