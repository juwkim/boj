import sys
input = sys.stdin.readline
from itertools import product

N = int(input())
A, B, C, D = zip(*[[*map(int, input().split())] for _ in range(N)])
p = sorted(sum(l) for l in product(A, B))
q = sorted(sum(l) for l in product(C, D))
l, r = 0, N * N - 1
ans = 0
while l < N * N and r >= 0:
    s = p[l] + q[r]
    if s == 0:
        a, b = 1, 1
        while l + a < N * N and p[l + a] == p[l]: a += 1
        while r - b >= 0 and q[r - b] == q[r]: b += 1
        ans += a * b
        l += a
        r -= b
    elif s < 0: l += 1
    else:       r -= 1
print(ans)