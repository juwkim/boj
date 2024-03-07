import sys
input = sys.stdin.readline
g = lambda: tuple(map(int, input().split()))
from collections import Counter

def dist(a, b):
    h1, m1, s1 = a
    h2, m2, s2 = b
    d = (h1 - h2) * 10**12 + (m1 - m2) * 10**6 + (s1 - s2)
    return d % (12 * 10**12)

n = int(input())
nums = []
cnt = Counter()
for _ in range(n):
    a = g()
    if cnt[a] == 0:
        nums.append(a)
    cnt[a] += 1
nums.sort()
cur = sum(dist(nums[0], nums[i]) * cnt[nums[i]] for i in range(1, len(nums)))
ans = cur
for i in range(1, len(nums)):
    p = dist(nums[i - 1], nums[i])
    if p:
        cur += (12 * 10**12 - p) * (n - cnt[nums[i]]) - p * cnt[nums[i]]
    ans = min(ans, cur)
ans, s = divmod(ans, 10**6)
h, m = divmod(ans, 10**6)
print(h, m, s)