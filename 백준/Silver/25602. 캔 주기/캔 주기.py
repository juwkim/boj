import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import product

N, K = g()
A = g()
R = [g() for _ in range(K)]
M = [g() for _ in range(K)]
ans = 0
for l in product(range(N), repeat=2*K):
    cnt = [0] * N
    for i in l:
        cnt[i] += 1
    if all(A[i] >= cnt[i] for i in range(N)):
        cur = sum(R[i][l[i]] + M[i][l[i + K]] for i in range(K))
        ans = max(ans, cur)
print(ans)