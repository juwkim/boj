g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())
ans = min(nums[i] + nums[2*N-1-i] for i in range(N))
print(ans)