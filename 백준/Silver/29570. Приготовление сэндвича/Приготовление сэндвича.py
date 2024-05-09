l = [bytearray(2001) for _ in range(2001)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 + 1000, x2 + 1000):
        for j in range(y1 + 1000, y2 + 1000):
            l[i][j] = 1
print(sum(sum(a) for a in l))