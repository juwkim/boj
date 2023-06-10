N = int(input())
a = int(input())
nums = [*map(int, input().split())]

if a == 2:
    ans = sum(num * num for num in nums)
else:
    ans = sum(num ** a for num in nums if num > 0)
print(ans)