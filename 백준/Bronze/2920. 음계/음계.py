nums = [*map(int, input().split())]
print('ascending' if nums == sorted(nums) else 'descending' if nums == sorted(nums, reverse=True) else 'mixed')