import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter
from itertools import combinations

cnt = Counter(input())
ans = +any(val >= 2 for val in cnt.values())
for a, b in combinations(cnt.values(), 2):
    ans += a * b
print(ans)