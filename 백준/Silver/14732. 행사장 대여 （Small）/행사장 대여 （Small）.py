g = lambda: [*map(int, input().split())]

Map = [[0]*500 for _ in range(500)]
for _ in range(int(input())):
    x1, y1, x2, y2 = g()
    for i in range(x1, x2):
        for j in range(y1, y2):
            Map[i][j] = 1

ans = 0
for line in Map:
    ans += sum(line)
print(ans)