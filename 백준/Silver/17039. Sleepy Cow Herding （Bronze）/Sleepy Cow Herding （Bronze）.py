g = lambda: [*map(int, input().split())]

nums = sorted(g())
a = nums[1] - nums[0]
b = nums[2] - nums[1]
if a == 1 and b == 1:
    print(0)
elif a == 2 or b == 2:
    print(1)
else:
    print(2)
print(max(a, b) - 1)