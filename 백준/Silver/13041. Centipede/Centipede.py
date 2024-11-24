import sys
input = sys.stdin.readline
from collections import Counter

for _ in range(int(input())):
    n, m = int(input()), int(input())
    a = []
    for _ in range(m):
        l, r = map(int, input().split())
        if l + r <= n:
            a.append((l, r))
    if not a:
        print(1, n - 1)
        continue
    a.append((10**9, 10**9))
    a.sort()
    keys = sorted({r for _, r in a})
    l, r = a[0]
    total, cnt = 1, Counter()
    cnt[r] = 1
    ans, Max, prev = (l, n - l), 1, l
    for l, r in a[1:]:
        if l != prev:
            while keys[-1] > n - prev:
                k = keys.pop()
                total -= cnt[k]
            if total > Max:
                Max = total
                ans = (prev, n - prev)
            prev = l
        cnt[r] += 1
        total += 1
    print(*ans)