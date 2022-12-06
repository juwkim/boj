g = lambda: [*map(int, input().split())]

R, C = g()
Map = [g() for _ in range(R)]
ans = 0
for i in range(R-1):
    for j in range(C-1):
        a, b, c, d = Map[i][j], Map[i][j+1], Map[i+1][j], Map[i+1][j+1]
        if a in [b, c, d]:
            ans = max(ans, a)
        if b in [c, d]:
            ans = max(ans, b)
        if c == d:
            ans = max(ans, c)
print(ans)