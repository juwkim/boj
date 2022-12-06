ans = 0
N = int(input())
nums = sorted(int(input()) for _ in range(N))
for i in range(N):
    ans += abs(i + 1 - nums[i])
print(ans)