import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, m = g()
a = [g() for _ in range(n)]
x = [max(l) for l in a]
y = [max(l) for l in zip(*a)]
print(sum(a[i][j] for i in range(n) for j in range(m) if a[i][j] != x[i] and a[i][j] != y[j]))