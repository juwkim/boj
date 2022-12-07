g = lambda: [*map(int, input().split())]
mod = 10 ** 9 + 7
N = int(input())
nums = g()
px = [0]
for num in nums:
    px.append(px[-1] + num)
ans = 0
for i in range(1, N):
    ans = (ans + nums[i] * px[i]) % mod
ans %= mod
print(ans)