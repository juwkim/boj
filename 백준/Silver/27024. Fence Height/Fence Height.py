N = int(input())
nums = sorted(int(input()) for _ in range(N))
s, t = 0, N // 2
ans = 1e9
while t < N:
    ans = min(ans, nums[t] - nums[s])
    t += 1
    s += 1
print(ans)