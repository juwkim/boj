from bisect import bisect_left
N = int(input())
nums = [*map(int, input().split())]
rank = sorted(nums)
for num in nums:
    print(bisect_left(rank, num) + 1)