import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect, bisect_left

N = int(input())
pos = sorted(int(input()) for _ in range(N))
ans = 0
for i in range(N):
    cur = i
    dist = 1
    while True:
        r = bisect(pos, pos[cur] + dist) - 1
        if r == cur or r == N - 1:
            break
        cur = r
        dist += 1
    cur = i
    dist = 1
    while True:
        l = bisect_left(pos, pos[cur] - dist)
        if l == cur:
            break
        cur = l
        dist += 1
    ans = max(ans, r - l + 1)
print(ans)