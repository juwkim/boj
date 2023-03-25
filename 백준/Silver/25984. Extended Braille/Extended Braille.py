g = lambda: [*map(int, input().split())]

Map = set()
for _ in range(int(input())):
    p = sorted(g() for _ in range(int(input())))
    a, b = p[0]
    q = tuple((s - a, t - b) for s, t in p)
    Map.add(q)
print(len(Map))