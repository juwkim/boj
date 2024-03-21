import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        cnt[tuple(sorted((s[i], s[i-1])))] += 1
M = max(cnt.values())
for k in cnt:
    if cnt[k] == M:
        print(*k, sep='')