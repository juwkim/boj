g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()

best, best_idx = 100, -1
for i in range(n-2):
    tmp = max(nums[i], nums[i+2])
    if tmp < best:
        best = tmp
        best_idx = i + 1
print(best_idx, best)