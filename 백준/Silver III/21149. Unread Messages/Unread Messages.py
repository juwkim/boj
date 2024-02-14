import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
ans, cnt = 0, Counter()
for i in range(m):
    s = int(input())
    ans += n + cnt[s] - i - 1
    cnt[s] = i + 1
    print(ans)