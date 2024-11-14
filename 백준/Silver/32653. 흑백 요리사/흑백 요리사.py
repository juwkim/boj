from math import lcm

N, *nums = map(int, open(0).read().split())
print(lcm(*[2 * x for x in nums]))