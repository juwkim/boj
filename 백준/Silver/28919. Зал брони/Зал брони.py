g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
x = g()
l, r = a[0], sum(a) - a[0]
d = sum(a[i] * (x[i] - x[0]) for i in range(1, n))
min_dist = d
ans = x[0]
for i in range(1, n):
    d += (l - r) * (x[i] - x[i - 1])
    l += a[i]
    r -= a[i]
    if d < min_dist:
        min_dist = d
        ans = x[i]
print(ans)