import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
N, L, H = g()
print(sum(sorted(g())[L:N-H])/(N-L-H))