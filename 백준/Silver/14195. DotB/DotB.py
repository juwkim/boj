g = lambda: map(int, input().split())
for _ in range(int(input())):
    n, c = g()
    nums = [*map(list, enumerate(g(), 1))]
    idx, d = 0, 1
    for _ in range(n + 4):
        if len(nums) == 1:
            break
        nums[idx][1] -= c
        if nums[idx][1] <= 0:
            nums.pop(idx)
            if d == -1: idx -= 1
            d = -d
        idx = (idx + d) % len(nums)
    print(nums[idx][0])