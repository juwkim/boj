import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from itertools import product
from collections import Counter

N, M = int(input()), int(input())
cnt = Counter(B - A for A, B in product(g(), g()) if B >= A)
k = max(cnt, key=lambda x: (cnt[x], -x)) if cnt else 0
print(k)