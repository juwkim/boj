nums = [*map(int, [input() for _ in range((int(input())))])]
s = sum(nums)//len(nums)
print(sum(max(s-num, 0) for num in nums))