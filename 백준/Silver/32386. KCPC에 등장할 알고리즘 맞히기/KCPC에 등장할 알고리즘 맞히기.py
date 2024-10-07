import sys
input = sys.stdin.readline
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    s, t, *l = input().split()
    for name in l:
        cnt[name] += 1
(k, v), *l = cnt.most_common(2)
if l and v == l[0][1]:
    print(-1)
else:
    print(k)