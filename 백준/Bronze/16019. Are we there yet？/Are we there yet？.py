d = [*map(int, input().split())]
nums = [*map(sum, [d[:i] for i in range(5)])]
for i in range(5):
    print(*nums)
    if i < 4:
        for j in range(i+1):
            nums[j] += d[i]
        for j in range(i+1, 5):
            nums[j] -= d[i]