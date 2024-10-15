P, N, *nums = map(int, open(0).read().split())
nums.sort()
ans, i, time = 0, 0, P - 1
while i < N and time - nums[i] >= 0:
    ans += time
    time -= nums[i]
    i += 1
print(i, ans)