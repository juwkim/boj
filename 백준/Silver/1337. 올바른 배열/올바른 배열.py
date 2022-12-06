ans = 1e9
l, r = 0, 0
N = int(input())
nums = sorted(int(input()) for _ in range(N))
while r < N:
    diff = nums[r] - nums[l]
    if diff <= 4:
        ans = min(ans, 4 - r + l)
        r += 1
    else:
        ans = min(ans, 4)
        l += 1
print(ans)