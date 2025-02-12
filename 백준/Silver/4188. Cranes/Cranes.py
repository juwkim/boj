import sys
input = sys.stdin.readline
from itertools import combinations

for _ in range(int(input())):
    C = int(input())
    x, y, r = zip(*[map(int, input().split()) for _ in range(C)])
    ans = 0
    for i in range(1, C + 1):
        for l in combinations(range(C), i):
            if all((x[a] - x[b])**2 + (y[a] - y[b])**2 > (r[a] + r[b])**2 for a, b in combinations(l, 2)):
                ans = max(ans, sum(r[p]**2 for p in l))
    print(ans)