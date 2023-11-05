import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, L = g()
print('1' * (L - 1) + str(N))