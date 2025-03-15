import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

for _ in range(int(input())):
    *cnt, X, Y = map(int, input().split())
    ans = 24
    patterns = [[] for _ in range(X)]
    for _ in range(5):
        for i, s in enumerate(input().split()):
            patterns[i].append(s)
    for l in combinations(patterns, Y):
        cur = 0
        for j in range(5):
            a = 0
            for i in range(5):
                if (i, j) == (2, 2):
                    continue
                a += any(p[i][j] == 'X' for p in l)
            cur += max(0, a - cnt[j])
        ans = min(ans, cur)
    print(ans)