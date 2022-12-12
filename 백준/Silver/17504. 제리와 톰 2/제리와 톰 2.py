g = lambda: [*map(int, input().split())]

from math import gcd
N = int(input())
*nums, q = g()
p = 1
for j in range(N - 2, -1, -1):
    q, p = q * nums[j] + p, q
GCD = gcd(q, p)
print((q - p) // GCD, q // GCD)