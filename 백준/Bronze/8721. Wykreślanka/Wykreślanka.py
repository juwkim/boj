n, i = int(input()), 1
nums = [*map(int, input().split())]
for num in nums:
    if num == i:
        n -= 1
        i += 1
print(n)