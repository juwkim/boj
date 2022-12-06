input()
nums = [*map(int, input().split())] + [0]
input()
for i in map(int, input().split()):
    nums[i-1] += nums[i-1] != 2019 and nums[i-1] + 1 != nums[i]
print(*nums[:-1], sep='\n')