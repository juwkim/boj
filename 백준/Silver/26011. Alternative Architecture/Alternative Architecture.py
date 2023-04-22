from math import isqrt

a, b = sorted(map(lambda x: int(x) - 1, input().split()))
ans = 1 + (a != b)
i = 1
while True:
    j2 = a * a - i * i
    if i * i >= j2:
        break
    j = isqrt(j2)
    if j ** 2 == j2:
        p, r = divmod(b * i, a)
        if r == 0 and p * j % i == 0:
            ans += [4, 2][a == b]
    i += 1
print(ans)