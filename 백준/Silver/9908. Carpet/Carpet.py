g = lambda: [*map(int, input().split())]

r, c = g()
Map = [[1] * c for _ in range(r)]
for _ in range(int(input())):
    i, j = g()
    Map[i-1][j-1] = 0
for i in range(r):
    for j in range(1, c):
        if Map[i][j]:
            Map[i][j] += Map[i][j-1]

ans = 0
for i in range(r):
    for j in range(c):
        l = 1e10
        for k in range(i, -1, -1):
            l = min(l, Map[k][j])
            ans = max(ans, l * (i - k + 1))
print(ans)