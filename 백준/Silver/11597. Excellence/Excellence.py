N = int(input())
nums = sorted(int(input()) for _ in range(N))
ans = 1e10
for i in range(N//2):
    tmp = nums[i] + nums[N-1-i]
    ans = min(ans, tmp)
print(ans)