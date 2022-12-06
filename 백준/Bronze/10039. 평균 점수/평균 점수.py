nums = [int(input()) for _ in range(5)]
total = 0
for num in nums:
    if num < 40:
        total += 40
    else:
        total += num
print(total // 5)
