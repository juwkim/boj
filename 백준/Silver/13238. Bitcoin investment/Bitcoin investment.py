g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
Max = 0
ans = 0
for i in range(N-1, -1, -1):
    Max = max(Max, nums[i])
    ans = max(ans, Max - nums[i])
print(ans)