from math import gcd
from itertools import combinations

ans = 1
for a, b in combinations(map(int, open(0).read().split()), 2):
    ans = max(ans, gcd(a, b))
print(ans)