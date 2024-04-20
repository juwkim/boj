from functools import cmp_to_key
N, *nums = open(0).read().split()
if all(c == '0' for c in nums):
    print(0)
else:
    print(*sorted(nums, key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1)), sep='')