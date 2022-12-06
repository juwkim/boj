g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = [0 for _ in range(N)]
idxs = [*range(N)]
for i in range(N):
    idx = idxs.pop(nums[i])
    ans[idx] = i + 1
print(*ans)