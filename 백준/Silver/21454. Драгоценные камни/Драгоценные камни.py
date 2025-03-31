import sys
from collections import defaultdict, Counter
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
S = input()
dic = defaultdict(list)
for _ in range(k):
    a, b = input()
    dic[b].append(a)

ans, cnt = 0, Counter()
for c in S:
    ans += sum(cnt[k] for k in dic[c])
    cnt[c] += 1
print(ans)