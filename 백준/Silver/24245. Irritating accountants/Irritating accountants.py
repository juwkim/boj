import sys
input = sys.stdin.readline
from collections import Counter

n, k = map(int, input().split())
cnt = Counter(input().split())
c = {s: i for i, s in enumerate(input().split())}
orders = [[] for _ in range(k)]
for _ in range(k):
    s, m, *names = input().split()
    orders[c[s]] = names
ans = []
for order in orders:
    for name in order:
        ans.extend([name] * cnt[name])
print(*ans)