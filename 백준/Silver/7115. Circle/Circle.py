dist2 = lambda x, y: x * x + y * y

k, r = map(int, input().split())
x, y = 0, (r - 1) // k
p = (r/k)**2
cnt = 4
while y > x:
    cnt += 8
    if p > dist2(x + 1, y):
        x += 1
    elif dist2(x, y - 1) < p < dist2(x + 1, y):
        y -= 1
    else:
        x += 1
        y -= 1
print(cnt)