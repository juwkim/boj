N = int(input())
nums = [*map(int, input().split())]

h = [0] * (N)
Min = nums[0]
for i in range(1, N - 1):
    if nums[i] < nums[i - 1]:
        Min = nums[i]
    h[i] = nums[i] - Min

Min = nums[-1]
for i in range(N - 2, 0, -1):
    if nums[i] < nums[i + 1]:
        Min = nums[i]
    h[i] = min(h[i], nums[i] - Min)
print(max(h))