import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

nums = g()
res = Counter(g())
ans = []
for _ in range(3):
    tmp = []
    for i in range(0, len(nums), 2):
        if res[nums[i]]:
            tmp.append(nums[i])
            res[nums[i]] -= 1
        else:
            tmp.append(nums[i+1])
            res[nums[i+1]] -= 1
    ans.append(tmp)
    nums = tmp
for l in ans[::-1]:
    print(*l)