import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

H, W = g()
nums = []
for i in range(H):
    if i & 1:
        nums.extend(reversed(g()))
    else:
        nums.extend(g())
check = bytearray(H * W // 2 + 1)
ans, i = H * W // 2, 0
while i < len(nums):
    if check[nums[i]]:
        i += 1
    elif nums[i] == nums[i + 1]:
        i += 2
    else:
        check[nums[i]] = 1
        check[nums[i + 1]] = 1
        i += 2
        ans += 1
print(ans)