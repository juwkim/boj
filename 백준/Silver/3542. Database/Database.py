import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    d = defaultdict(lambda: defaultdict(int))
    for r in range(1, n + 1):
        l = input().split(',')
        for c1 in range(m - 1):
            for c2 in range(c1 + 1, m):
                if (l[c1], l[c2]) in d[(c1, c2)]:
                    print("NO")
                    print(d[(c1, c2)][(l[c1], l[c2])], r)
                    print(c1 + 1, c2 + 1)
                    return
                d[(c1, c2)][(l[c1], l[c2])] = r
    print("YES")
    return
solve()