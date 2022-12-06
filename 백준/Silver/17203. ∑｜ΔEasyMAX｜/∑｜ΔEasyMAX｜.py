g = lambda: [*map(int, input().split())]
N, Q = g()
nums = g()
for i in range(N - 1, 0, -1):
    nums[i] = abs(nums[i] - nums[i - 1])
for i in range(2, N):
    nums[i] += nums[i - 1]
nums[0] = 0
for _ in range(Q):
    i, j = g()
    print(nums[j-1] - nums[i-1])