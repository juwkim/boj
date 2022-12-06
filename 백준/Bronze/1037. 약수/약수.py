import math
n = int(input())

t = 1
nums = [*map(int, input().split())]
for num in nums:
    t = t * num // math.gcd(t, num)
if t in nums:
    t *= min(nums)
print(t)