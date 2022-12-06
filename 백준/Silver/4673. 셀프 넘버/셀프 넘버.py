def dsum(n):
    digits = list(map(int, list(str(n))))
    return n + sum(digits)

nums = [num for num in range(1, 10000)]

for num in range(1, 10000):
    if dsum(num) in nums:
        nums.remove(dsum(num))

for num in nums:
    print(num)