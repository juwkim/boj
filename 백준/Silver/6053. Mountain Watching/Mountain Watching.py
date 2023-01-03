N = int(input())
nums = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    if (i == 0 or nums[i] >= nums[i-1]) and (i == N - 1 or nums[i] >= nums[i+1]):

        left = i - 1
        while left >= 0 and nums[left + 1] >= nums[left]:
            left -= 1
            
        right = i + 1
        while right <= N - 1 and nums[right - 1] >= nums[right]:
            right += 1

        ans = max(ans, right - left - 1)
print(ans)