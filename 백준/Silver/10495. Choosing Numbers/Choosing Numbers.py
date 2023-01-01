def g(): return [*map(int, input().split())]

from math import gcd

while True:
    try:
        n, *nums = g()
        nums = sorted(nums, reverse=True)
        idx = 0
        while any(gcd(nums[idx], nums[i]) != 1 for i in range(n) if i != idx):
            idx += 1
        print(nums[idx])
    except:
        break