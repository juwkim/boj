import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
cnt = Counter()
total = 0
lo, hi = 0, 0
for _ in range(N):
    for num in map(int, input().split()):
        cnt[num] += 1
        total += num
        hi = max(hi, num)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if 2 * sum(min(num, mid) * freq for num, freq in cnt.items()) >= total:
        hi = mid
    else:
        lo = mid
print(hi)