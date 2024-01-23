import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, K = g()
ans = (N + K - M - 1) // (K - M)
print(ans)