import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, K = g()
nums = [tuple(g() + [-i]) for i in range(N)]
d = {v: i for i, v in enumerate(sorted(nums, reverse=True))}
ans, cnt = 0, 0
for p in nums:
    if d[p] < K:
        cnt += 1
        if cnt == K:
            break
    else:
        ans += 1
print(ans)