import sys
input = sys.stdin.readline
from collections import Counter, defaultdict

d = defaultdict(Counter)
n, m = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    d[a][b] += 1
    if a != b:
        d[b][a] += 1
keys = sorted(d.keys())
for _ in range(m):
    i = int(input())
    ans = 0
    l, r = 0, len(keys) - 1
    while l <= r:
        if keys[l] + keys[r] == i:
            if l == r:
                ans += sum(v // 2 for v in (d[keys[l]] & d[keys[r]]).values())
            else:
                ans += sum((d[keys[l]] & d[keys[r]]).values())
            l += 1
            r -= 1
        elif keys[l] + keys[r] < i:
            l += 1
        else:
            r -= 1
    print(ans)