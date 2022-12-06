g = lambda: [*map(int, input().split())]

N, K, B = g()
nums = g()
B %= N
ans = 0
for i in range(B-1, B+K-1):
    ans += nums[i%N]
print(ans)