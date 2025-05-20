from math import gcd
from itertools import pairwise

N, *nums = map(int, open(0).read().split())
diff = [b - a for a, b in pairwise(nums)]
g = gcd(*diff)
print(sum(d // g - 1 for d in diff))