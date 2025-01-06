import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, k = g()
x, y = zip(*[g() for _ in range(n)])
xsum, ysum = sum(x), sum(y)
for i in range(k - 1):
    xsum += xsum / n - x[i]
    ysum += ysum / n - y[i]
print(xsum / n, ysum / n)