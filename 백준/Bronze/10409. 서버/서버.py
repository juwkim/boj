n, T = map(int, input().split())
nums = [*map(int, input().split())]
count = 0
for num in nums:
    T -= num
    if T < 0:
        break
    count += 1
print(count)