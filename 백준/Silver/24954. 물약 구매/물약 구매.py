import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from itertools import permutations

N = int(input())
c = g()
nums = [[g() for _ in range(int(input()))] for _ in range(N)]
ans = 1e9
for p in permutations(range(N)):
    cost, cur = c[:], 0
    for i in p:
        cur += cost[i]
        for a, d in nums[i]:
            cost[a-1] = max(1, cost[a-1] - d)
    ans = min(ans, cur)
print(ans)