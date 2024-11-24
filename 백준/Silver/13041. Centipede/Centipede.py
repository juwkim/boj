import sys
input = sys.stdin.readline
from collections import Counter

for _ in range(int(input())):
    n, m = int(input()), int(input())
    a = []
    for _ in range(m):
        l, r = map(int, input().split())
        if l + r <= n: a.append((l, r))
    a.append((10**9, 10**9))
    a.sort()

    keys = sorted({r for _, r in a})
    total, cnt = 0, Counter()
    ans, Max, prev = (1, n - 1), 0, 0
    for l, r in a:
        if l != prev:
            while keys and keys[-1] > n - prev:
                total -= cnt[keys.pop()]
            if total > Max:
                ans, Max = (prev, n - prev), total
            prev = l
        cnt[r] += 1
        total += 1
    print(*ans)