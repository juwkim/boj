def cal(nums):
    res = 1
    for num in nums:
        res *= num
    return res

N = int(input())
nums = [*map(int, input().split())]
ans = 0
for a in range(1, N-2):
    q = cal(nums[:a])
    for b in range(a+1, N-1):
        w = cal(nums[a:b])
        for c in range(b+1, N):
            e = cal(nums[b:c])
            r = cal(nums[c:])
            ans = max(ans, q + w + e + r)
print(ans)