import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

N, M = g()
K = 1000
for _ in range(M):
    L, R = g()
    K = min(K, R - L + 1)
for i in range(N):
    print(i % K + 1, end=' ')