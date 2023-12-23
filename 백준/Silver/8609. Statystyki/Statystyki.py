import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import re

n = int(input())
nums = g()
s = input()
ans = []
for num in nums:
    if num == 1:
        ans.append(s.count(' '))
    elif num == 2:
        ans.append(len(re.findall(r'\d+', s)))
    elif num == 3:
        ans.append(len(re.findall(r'(?<![a-zA-Z])[a-zA-Z]+(?![a-zA-Z])', s)))
    elif num == 4:
        ans.append(len(re.findall(r'[^.]*[a-zA-Z]+[^.]*\.', s)))
    elif num == 5:
        words = map(str.lower, re.findall(r'(?<![a-zA-Z])[a-zA-Z]+(?![a-zA-Z])', s))
        ans.append(sum(word == word[::-1] for word in words))
print(*ans)