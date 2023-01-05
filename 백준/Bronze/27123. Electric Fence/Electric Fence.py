from math import gcd

n, m, p = map(int, input().split())
b = gcd(n, m) + gcd(0, p) + gcd(m, n - p)
ans = (p * m - b) // 2 + 1
print(ans)