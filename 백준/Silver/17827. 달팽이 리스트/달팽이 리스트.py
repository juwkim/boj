import sys
input = sys.stdin.readline
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, V = g()
C = g()
for _ in range(M):
    K = int(input())
    if K < N:
        print(C[K])
    else:
        print(C[(K - V + 1) % (N - V + 1) + V - 1])