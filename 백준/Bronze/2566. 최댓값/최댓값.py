nums = [list(map(int, input().split())) for _ in range(9)]
max_nums = [max(i) for i in nums]
k = max(max_nums)
a = max_nums.index(k)
b = nums[a].index(k)
print(k)
print(a+1, b+1)