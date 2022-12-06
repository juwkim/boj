n = int(input())
nums = [*map(int, input().split())]
max_count, now, i, check = 0, 0, 1, nums[0]
while i < n:
    if check > nums[i]:
        now += 1
    else:
        max_count = max(max_count, now)
        check, now = nums[i], 0
    i += 1
print(max(max_count, now))