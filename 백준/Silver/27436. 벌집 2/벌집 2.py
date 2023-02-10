from math import isqrt

N = int(input())
tmp = isqrt(num:= 12 * N - 3)
ans = (3 + tmp) // 6 + (num != tmp ** 2 or tmp % 6 != 3)
print(ans)