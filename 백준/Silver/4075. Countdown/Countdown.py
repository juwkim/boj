import sys
input = sys.stdin.readline
from collections import Counter

for tc in range(1, 1 + int(input())):
    n, d = map(int, input().split())
    p = {}
    for _ in range(n):
        name, m, *dnames = input().split()
        for dname in dnames:
            p[dname] = name
    cnt = Counter()
    for name in p:
        cur = name
        for _ in range(d):
            if cur not in p:
                break
            cur = p[cur]
        else:
            cnt[cur] += 1
    l = sorted([(m, name) for name, m in cnt.items()], key=lambda x: (-x[0], x[1]))
    print(f"Tree {tc}:")
    for i, (m, name) in enumerate(l):
        if m == 0 or (i >= 3 and m != l[2][0]):
            break
        print(f"{name} {m}")
    print()