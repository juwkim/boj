g = lambda: [*map(int, input().split())]

n, r = g()
Map = [[0] * n for _ in range(n)]
for i in range(n):
    for j, num in enumerate(g()):
        if num == 1:
            for a in range(max(0, i - r), min(n, i + r + 1)):
                for b in range(max(0, j - r), min(n, j + r + 1)):
                    Map[a][b] += 1
for line in Map:
    print(*line)