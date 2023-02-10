from math import isqrt

N = int(input())
num = 12 * N - 3
tmp = isqrt(num)
if num == tmp ** 2 and tmp % 6 == 3:
    ans = (3 + tmp) // 6
else:
    ans = (3 + tmp) // 6 + 1
print(ans)