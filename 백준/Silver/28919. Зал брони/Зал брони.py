g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
x = g()
d = sum(a[i] * (x[i] - x[0]) for i in range(1, n))
ans, min_dist, cnt = x[0], d, 2 * a[0] - sum(a)
for i in range(1, n):
    d += cnt * (x[i] - x[i - 1])
    cnt += 2 * a[i]
    if d < min_dist:
        ans, min_dist = x[i], d
print(ans)