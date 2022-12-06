g = lambda: [*map(int, input().split())]

n = int(input())
rec = []
for _ in range(n):
    x1, y1, x2, y2 = g()
    rec.append(sorted([x2 - x1, y2 - y1]))

cnt = 0
for i in range(n-1):
    x1, y1 = rec[i]
    for j in range(i+1, n):
        x2, y2 = rec[j]
        if x1 > x2:
            cnt += y1 < y2
        elif x1 < x2:
            cnt += y1 > y2
print(cnt)