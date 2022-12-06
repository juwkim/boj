n = int(input())
nums = [*map(int, input().split())]
s = max(nums)
for i in range(n):
    if s == nums[i]:
        print(chr(ord('A') + i), end='')