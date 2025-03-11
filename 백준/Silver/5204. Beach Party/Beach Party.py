import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from itertools import combinations

for tc in range(1, 1 + int(input())):
    s, m, n = g()
    nums = []
    for _ in range(n):
        idx = [0] * (m + 1)
        for i, num in enumerate(g()):
            idx[num] = i
        nums.append(idx)
    me, *friends = nums
    ans = 0
    for l in combinations(range(1, m + 1), s):
        num = min(l, key=lambda x: me[x])
        cnt = 1 + sum(num == min(l, key=lambda x: friend[x]) for friend in friends)
        ans = max(ans, cnt)
    print(f"Data Set {tc}:\n{ans}")