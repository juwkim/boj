import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import decimal

N, K = g()
nums = []
for _ in range(N):
    nums.append(decimal.Decimal(input()))
nums.sort()

m0 = sum(nums[K:-K] if K else nums) / decimal.Decimal(N - 2 * K)
print("%.2f" % (m0 + decimal.Decimal("0.00000001")))

for i in range(K):
    nums[i] = nums[K]
    nums[-i - 1] = nums[-K - 1]

m1 = sum(nums) / decimal.Decimal(N)
print("%.2f" % (m1 + decimal.Decimal("0.00000001")))