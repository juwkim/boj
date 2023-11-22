import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, K = g()
print((sum(g()) + M - 1) // M)