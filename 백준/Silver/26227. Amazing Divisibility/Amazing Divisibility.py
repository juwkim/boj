input()
l = [[0] * 7 for _ in range(11)]
for a in input().split():
    l[len(a)][int(a) % 7] += 1
ans = 0
for i in range(11):
    for j in range(7):
        for x in range(11):
            for y in range(7):
                if (i, j) == (x, y):
                    if (j * pow(10, x, 7) + y) % 7 == 0:
                        ans += l[i][j] * (l[i][j] - 1)
                else:
                    if (j * pow(10, x, 7) + y) % 7 == 0:
                        ans += l[i][j] * l[x][y]
print(ans)