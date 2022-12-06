from math import lcm
nums = [int(input()) for _ in range(int(input()))]
LCM = lcm(*nums)
for num in nums: print(LCM // num)