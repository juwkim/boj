import sys
input = sys.stdin.readline
from collections import Counter
from math import comb

for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = Counter()
    for s in input().split():
        cnt[("".join(sorted(s.lower())), sum(c.isupper() for c in s))] += 1
    print(sum(comb(v, 2) for v in cnt.values()))