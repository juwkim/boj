g = lambda: [*map(int, input().split())]

from math import gcd
for _ in range(1, 1 + int(input())):
    N, *nums = g()
    GCD = abs(nums[0] - nums[1])
    for i in range(1, N-1):
        GCD = gcd(GCD, nums[i] - nums[i+1])
    q = nums[0] % GCD
    if q == 0:
        ans = 0
    else:
        ans = GCD - q
    print(f'Case #{_}: {ans}')