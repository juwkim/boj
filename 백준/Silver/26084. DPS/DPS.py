import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
from math import comb

a, b, c = sorted(input())
cnt = Counter([input()[0] for _ in range(int(input()))])
if a == b == c:
    print(comb(cnt[a], 3))
elif a == b:
    print(comb(cnt[a], 2) * cnt[c])
elif b == c:
    print(cnt[a] * comb(cnt[b], 2))
else:
    print(cnt[a] * cnt[b] * cnt[c])