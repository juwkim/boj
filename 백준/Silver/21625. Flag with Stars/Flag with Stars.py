from math import isqrt

n = int(input())
t = isqrt(n)
while t > 1 and n % t: t -= 1

a, b, i = abs(t - n // t), n - 1, 2
while i * i <= 2 * n:
    q, r = divmod(i, 2)
    good = False
    if r and (n + q + 1) % i == 0:
        k = (n + q + 1) // i
        good = True
    if (n + q) % i == 0:
        k = (n + q) // i
        good = True
    if good:
        num = abs(i - k)
        if num >= b:
            break
        b = num
    i += 1
print(min(a, b))