N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)

r, q = divmod(N, 3)
ans = sum(nums[N-1-i] for i in range(q))

for i in range(0, 3*r, 3):
    ans += nums[i] + nums[i+1]
print(ans)