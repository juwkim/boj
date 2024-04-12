N, *nums = map(int, open(0).read().split())
nums.sort()
ans, w = 0, 2
l, r = 1, N - 2
for _ in range(1, N):
    ans = (ans + (w - 1) * (nums[l] - nums[r])) % 1_000_000_007
    w <<= 1; l += 1; r -= 1
print(ans)