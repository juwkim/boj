import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import Counter

n = int(input())
score = g()
nums = g()
cnt = Counter(nums)
ans, low = None, -1
for i in range(1, 102):
    cnt[i] += 1
    l = [k for k in cnt if cnt[k] == 1]
    if l:
        num = min(l)
        idx = -1 if num == i else nums.index(num)
        score[idx] += num
        c = sum(a < score[-1] for a in score)
        if c > low:
            ans, low = i, c
        score[idx] -= num
    else:
        c = sum(a < score[-1] for a in score)
        if c > low:
            ans, low = i, c
    cnt[i] -= 1
print(ans)