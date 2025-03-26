import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from itertools import pairwise

N, K = int(input()), int(input())
nums = sorted(sorted(g()) for _ in range(K))
M = int(input())
a, visited = 0, bytearray(K)
for _ in range(M):
    X, Y = sorted(g())
    check = False
    for i in range(K):
        P, Q = nums[i]
        if Y <= P or X >= Q:
            continue
        visited[i] = 1
        check = True
    a += check
print(a)
print(sum(visited))
ans = max(nums[0][0], N + 1 - nums[-1][1])
for (_, e), (s, _) in pairwise(nums):
    ans = max(ans, s - e + 1)
print(ans)