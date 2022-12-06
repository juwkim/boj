g = lambda: [*map(int, input().split())]

fishes = []
s, n = g()
x, y = 0, 0

for _ in range(n):
    fish = g()
    x, y = max(x, fish[0]), max(y, fish[1])
    fishes.append(fish)

Map = [[0] * y for _ in range(x)]
for i, j in fishes:
    Map[i-1][j-1] = 1

ans = 0
for p in range(0, max(1, x - s)):
    for q in range(0, max(1, y - s)):
        cur = sum(Map[i][j] for i in range(p, min(x, p+s+1)) for j in range(q, min(y, q+s+1)))
        ans = max(ans, cur)
print(ans)