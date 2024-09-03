N, K, *nums = map(int, open(0).read().split())
ans = 0
for i in range(N // 2):
    q, r = divmod(abs(nums[i] - nums[N - 1 - i]), K)
    ans += q + min(r, K - r + 1)
print(ans)