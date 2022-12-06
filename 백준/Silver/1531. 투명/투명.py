g = lambda: [*map(int, input().split())]

Map = [[0] * 101 for _ in range(101)]
N, M = g()
for _ in range(N):
    x1, y1, x2, y2 = g()
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            Map[i][j] += 1
print(sum(sum(i > M for i in line) for line in Map))