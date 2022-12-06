from itertools import combinations
N, M = map(int, input().split())
nums = [[*map(int, input().split())] for _ in range(N)]
ans = 0
for a, b, c in combinations(range(M), 3):
    cur = 0
    for l in nums:
        cur += max(l[a], l[b], l[c])
    ans = max(ans, cur)
print(ans)