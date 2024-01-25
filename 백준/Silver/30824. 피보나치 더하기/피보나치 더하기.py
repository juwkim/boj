import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product

a, b = 1, 1
nums1 = [1]
while b < 10 ** 16:
    a, b = b, a + b
    nums1.append(b)
nums2 = [sum(l) for l in product(nums1, repeat=2)]
nums3 = [sum(l) for l in product(nums1, repeat=3)]

nums = [[], set(nums1), set(nums2), set(nums3)]
for _ in range(int(input())):
    k, x = g()
    if x in nums[k]:
        print('YES')
    else:
        print('NO')