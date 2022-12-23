from bisect import bisect_left
from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    name, amount = input().split()
    dic[name] += int(amount)

ans = 'Not Delicious...'
nums = sorted(dic.values())
idx = 0
for i in range(len(nums)):
    num = int(nums[i] * 1.618)
    idx = bisect_left(nums, num, idx)
    if idx == len(nums):
        break
    if i != idx and nums[idx] == num:
        ans = 'Delicious!'
        break
print(ans)