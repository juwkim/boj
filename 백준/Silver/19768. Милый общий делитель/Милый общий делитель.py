from math import gcd, isqrt
num = gcd(*map(int, input().split()))
ans = 0
for i in range(1, 1 + isqrt(num)):
    q, r = divmod(num, i)
    if r == 0:
        ans = max(ans, i, q, key=lambda x: sum(int(a) for a in str(x)))
print(ans)