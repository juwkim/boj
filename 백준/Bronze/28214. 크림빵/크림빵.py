g = lambda: [*map(int, input().split())]

N, K, P = g()
nums = g()
ans = 0
for i in range(0, N * K, K):
    if nums[i:i+K].count(0) < P:
        ans += 1
print(ans)