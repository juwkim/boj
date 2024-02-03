g = lambda: map(int, input().split())
n, m = g()
a, t = 0, 0
for i, h in enumerate(g(), 1):
    if h >= m: t = i
    a += t
print(a)