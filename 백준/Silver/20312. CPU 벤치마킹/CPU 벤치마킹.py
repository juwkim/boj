N, *nums = map(int, open(0).read().split())
ans, cur = 0, 0
for i in range(N - 2, -1, -1):
    cur = (cur + 1) * nums[i] % 1_000_000_007
    ans = (ans + cur) % 1_000_000_007
print(ans)