nums = [*map(int, input().split(":"))]
print(int(all(i < 60 for i in nums)) and 2 * sum(1 <= int(i) <= 12 for i in nums))