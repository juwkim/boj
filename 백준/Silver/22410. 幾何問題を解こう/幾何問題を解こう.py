from math import gcd

p, q = map(int, input().split())
a = q // gcd(p, q)
ans = 1
for i in range(2, int(a**.5) + 1):
    if a % i == 0:
        ans *= i
        while a % i == 0:
            a //= i
if a > 1:
    ans *= a
print(ans)