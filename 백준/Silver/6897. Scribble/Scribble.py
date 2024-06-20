import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

point, cnt = {}, Counter()
for _ in range(int(input())):
    a, s, r = input().split()
    point[a], cnt[a] = int(s), int(r)

ans = 0
for _ in range(int(input())):
    c = Counter(input())
    if all(c[k] <= cnt[k] for k in c):
        ans = max(ans, sum(c[k] * point[k] for k in c))
print(ans)