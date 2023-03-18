N = int(input())
nums = [*map(int, input().split())]
nums.remove(0)

Max, cur = 0, 0
idx = N - 1
for i in range(N - 2, -1, -1):
    cur += nums[i]
    if cur > Max:
        Max = cur
        idx = i
nums.insert(idx, 0)

ans = 0
for i, num in enumerate(nums, 1):
    ans += i * num
print(ans)