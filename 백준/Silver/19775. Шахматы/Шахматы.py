n = int(input())
nums = [*map(int, input().split())]
for i in range(n):
    if nums[i] <= i:
        n = i
        break
print(n)
for i in range(1, 1 + n):
    print(i, i)