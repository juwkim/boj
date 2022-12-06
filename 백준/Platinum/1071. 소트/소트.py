from collections import*
input()
dic = Counter(map(int, input().split()))
nums = sorted(dic.keys())
prev = -2
while nums:
    if len(nums) == 1: idx = 0
    elif prev + 1 == nums[0] or (len(nums) == 2 and nums[0] + 1 == nums[1]): idx = 1
    else: idx = 0
    prev = nums[idx]
    print(nums[idx], end=' ')
    dic[nums[idx]] -= 1
    if dic[nums[idx]] == 0: del nums[idx]