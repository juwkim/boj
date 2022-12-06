input()
nums = [*map(int, input().split())]
print(1, end=' ')
for num in sorted(nums):
    print(nums.index(num) + 2, end=' ')