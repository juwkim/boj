import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m, k = g()
x, y = [0, n], [0, m]
for _ in range(k):
    t, v = g()
    if t:
        y.append(v)
    else:
        x.append(v)
x.sort()
y.sort()
p = max(x[i + 1] - x[i] for i in range(len(x) - 1))
q = max(y[i + 1] - y[i] for i in range(len(y) - 1))
print(min(p, q))