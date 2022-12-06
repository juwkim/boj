from itertools import combinations
from math import gcd
lcm = lambda a, b: a * b // gcd(a, b)
lcm_3 = lambda x: lcm(x[0], lcm(x[1], x[2]))
nums = [*map(int, input().split())]
print(min(lcm_3(i) for i in combinations(nums, 3)))