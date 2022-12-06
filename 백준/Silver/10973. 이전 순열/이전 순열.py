g = lambda: [*map(int, input().split())]


N = int(input())
nums = g()

idx = N - 1
while idx and nums[idx-1] <= nums[idx]:
    idx -= 1
if idx == 0:
    print(-1)
else:
    idx2 = N - 1
    while nums[idx - 1] <= nums[idx2]:
        idx2 -= 1
    
    nums[idx - 1], nums[idx2] = nums[idx2], nums[idx - 1]
    
    ans = nums[:idx] + nums[idx:][::-1]
    print(*ans)