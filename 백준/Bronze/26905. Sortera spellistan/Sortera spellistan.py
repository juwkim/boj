N = int(input())
nums = [int(input()) for _ in range(N)]
ans = 0
for i in range(N - 1):
    j = min(range(i, N), key=lambda x: nums[x])
    if j > i:
        ans += j - i
        tmp = nums[j]
        del nums[j]
        nums.insert(i, tmp)
print(ans)