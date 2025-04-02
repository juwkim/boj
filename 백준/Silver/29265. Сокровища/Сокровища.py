n, x, y, a, b, c, d = map(int, open(0).read().split())
px = [0] * (n + 1)
px[1], px[2] = x, x + y
t1, t2 = x, y
for i in range(3, n + 1):
    t1, t2 = t2, (a * t1 + b * t2 + c) % d
    px[i] += px[i-1] + t2
half_sum = px[n] + 1 >> 1
l = 0
ans = 1, n
for r in range(n):
    while px[r + 1] - px[l] >= half_sum:
        if r - l < ans[1] - ans[0]:
            ans = l + 1, r + 1
        l += 1
print(*ans)