import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K = g()
l = [*range(1, N + 1)]
for _ in range(K):
    A, B, C = g()
    pick = l[A - 1:B]
    l = l[:A - 1] + l[B:]
    l = l[:C] + pick + l[C:]
print(*l[:10])