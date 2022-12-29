g = lambda: [*map(int, input().split())]
n, d = g()
nums = bytearray(n)
for num in g():
    for i in range(max(0, num - 1 - d), min(n, num + d)):
        nums[i] = 1
print(sum(nums))