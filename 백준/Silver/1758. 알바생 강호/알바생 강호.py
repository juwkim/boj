N = int(input())
nums = sorted([int(input()) for _ in range(N)], reverse=True)
ans = sum(max(0, nums[i] - i) for i in range(N))
print(ans)