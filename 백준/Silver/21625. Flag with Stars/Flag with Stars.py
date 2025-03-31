from math import isqrt

n = int(input())
t = isqrt(n)
while t > 1 and n % t: t -= 1

a, b, i = abs(t - n // t), n - 1, 2
while i * i <= 2 * n:
    q, r = divmod(i, 2)
    good = False
    if r:
        if (n - q) % (2 * q + 1) == 0:
            k = (n - q) // (2 * q + 1) + 1
            good = True
        if (n - q - 1) % (2 * q + 1) == 0:
            k = (n - q - 1) // (2 * q + 1) + 1
            good = True
    elif (n - q) % (2 * q) == 0:
        k = (n - q) // (2 * q) + 1
        good = True
    if good:
        num = abs(i - k)
        if num >= b:
            break
        b = num
    i += 1
print(min(a, b))