g = lambda: [*map(int, input().split())]

from math import gcd
N = int(input())
r, *nums = g()
for num in nums:
    GCD = gcd(r, num)
    a = r // GCD
    num //= GCD
    print(f'{a}/{num}')