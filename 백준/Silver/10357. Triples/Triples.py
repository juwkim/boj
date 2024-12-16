from math import isqrt

m, n = map(int, open(0))
ans = (m + 1) * (n - 1)
for x in range(1, m):
    for y in range(x + 1, m):
        z = isqrt(x * x + y * y)
        if y <= z <= m and x * x + y * y == z * z:
            ans += 1
print(ans)