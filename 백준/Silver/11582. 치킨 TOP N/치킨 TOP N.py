g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
k = int(input())
for i in range(0, N, N // k):
    nums[i:i+N//k] = sorted(nums[i:i+N//k])
print(*nums)