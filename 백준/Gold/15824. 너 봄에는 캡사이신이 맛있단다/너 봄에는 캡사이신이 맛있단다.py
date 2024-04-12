N, *nums = map(int, open(0).read().split())
nums.sort()
ans, w, m = 0, 2, 1_000_000_007
l, r = 1, N - 2
for _ in range(1, N):
    ans = (ans + (w - 1) * (nums[l] - nums[r])) % m
    w = (w << 1) % m; l += 1; r -= 1
print(ans)