import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

s, e = [], []
for _ in range(int(input())):
    h1, m1, h2, m2 = g()
    s.append((h1, m1))
    e.append((h2, m2))
p, q = max(s), min(e)
if p < q:
    print("TAIP")
    print(*p, *q)
else:
    print("NE")