g = lambda: [*map(int, input().split())]
n, m, r, l = g()
r2, l2 = r**2, l**2
s = [g() for _ in range(n)]
t = [g() for _ in range(m)]
b = [0] * n
for i in range(n):
    x1, y1 = s[i]
    d2 = x1**2 + y1**2
    p = 2 + (d2 > r2)
    z = 0
    for j in range(m):
        x2, y2, num = t[j]
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= l2:
            z += num
    b[i] = p / (d2 * (1 + z))
print(*sorted(range(1, n + 1), key=lambda x: -b[x-1]))