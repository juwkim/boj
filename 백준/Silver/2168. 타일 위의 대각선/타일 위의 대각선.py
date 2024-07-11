from math import gcd

x, y = sorted(map(int, input().split()))
g = gcd(x, y)
ans = 0
for i in range(x // g):
    a, b = y * i // x, (y * (i + 1) + x - 1) // x,
    ans += b - a
ans *= g
print(ans)