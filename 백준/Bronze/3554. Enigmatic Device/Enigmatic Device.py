g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()

for _ in range(int(input())):
    ops, a, b = g()
    if ops == 1:
        for i in range(a-1, b):
            nums[i] = nums[i] * nums[i] % 2010
    else:
        print(sum(nums[a-1:b]))