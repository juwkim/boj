N = int(input())
nums = sorted([int(input()) for _ in range(N)], reverse=True)
ans = max((i + 1) * nums[i] for i in range(N))
print(ans)