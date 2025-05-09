dist2 = lambda x, y: x * x + y * y

k, r = map(int, input().split())
x1, y1 = 0, (r - 1) // k
x2 = y2 = int(r / (k * 2**.5))
p = (r/k)**2
cnt = 4
while (x1, y1) != (x2, y2):
    cnt += 8
    if p > dist2(x1 + 1, y1):
        x1 += 1
    elif dist2(x1, y1 - 1) < p < dist2(x1 + 1, y1):
        y1 -= 1
    else:
        x1 += 1
        y1 -= 1
print(cnt)