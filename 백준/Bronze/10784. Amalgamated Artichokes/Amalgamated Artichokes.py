from math import sin, cos
p, a, b, c, d, n = map(int, input().split())
max_price, ans = -2, 0
for k in range(1, 1 + n):
    val = sin(a * k + b) + cos(c * k + d)
    max_price = max(max_price, val)
    ans = max(ans, max_price - val)
print(p * ans)