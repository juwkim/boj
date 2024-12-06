import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, L = g()
x = g()
w = g()
print(sum(x[i] * w[i] for i in range(N)) / sum(w))