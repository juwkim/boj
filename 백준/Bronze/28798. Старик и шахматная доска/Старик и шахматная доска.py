from math import isqrt

n, m = sorted(map(int, input().split()))
a = isqrt(2 * n)
a += a % 2 == 0 and n >= a * a // 2 + a and m >= a * a // 2 + a + 1
print(a)