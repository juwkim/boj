ans = 1e10
N = int(input())
nums = [int(input()) for _ in range(N)]
for i in range(N-1):
    for j in range(i, N):
        tmp = sum(min((nums[i] - nums[k]) ** 2, (nums[j] - nums[k]) ** 2) for k in range(N))
        ans = min(ans, tmp)
print(ans)