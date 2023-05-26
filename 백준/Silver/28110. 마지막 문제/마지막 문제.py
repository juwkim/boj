N = int(input())
nums = sorted(map(int, input().split()))
idx = max(range(N - 1), key=lambda x: nums[x + 1] - nums[x] >> 1)
a, b = nums[idx], nums[idx + 1]
if b - a == 1:
    print(-1)
else:
    print((b + a) >> 1)