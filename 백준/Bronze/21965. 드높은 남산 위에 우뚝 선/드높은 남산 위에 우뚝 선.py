N = int(input())
nums = [*map(int, input().split())]
a = [(i < j) - (i > j) for i, j in zip(nums, nums[1:])]
b = [i + j for i, j in zip(a, a[1:])]
if b.count(0) <= 1 and not (set(b) - {0, 2, -2}):
    print('YES')
else:
    print('NO')