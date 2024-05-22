import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a, b = 0, 0
for _ in range(int(input())):
    m, k = g()
    s, t = [], []
    for _ in range(m):
        x, y = g()
        s.append(x * x + y * y)
    for _ in range(k):
        x, y = g()
        t.append(x * x + y * y)
    p, q = min(s), min(t)
    if p < q:
        a += sum(c < q for c in s)
    elif p > q:
        b += sum(c < p for c in t)
print(f"{a}:{b}")