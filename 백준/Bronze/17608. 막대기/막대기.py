import sys
nums = [*map(int, sys.stdin.read().split()[1:])][::-1]
s, count = 0, 0
for num in nums:
    if num > s:
        s = num
        count += 1
print(count)