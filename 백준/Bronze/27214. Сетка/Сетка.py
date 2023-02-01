k, w, h, t = map(int, open(0))
ans = [['*'] * (w * (t + k) + t) for _ in range(h * (t + k) + t)]

for i in range(t, t + (t + k) * h, t + k):
    for j in range(t, t + (t + k) * w, t + k):
        for x in range(i, i + k):
            for y in range(j, j + k):
                ans[x][y] = '.'        

for line in ans:
    print(*line, sep='')