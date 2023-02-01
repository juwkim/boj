N = int(input())
nums = [*map(int, input().split())]
Min, Max = min(nums), max(nums)
for num in nums:
    print(max(Max - num, num - Min))