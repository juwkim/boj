import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import defaultdict

N, M = g()
dic = defaultdict(list)
for i in range(N):
    k, *A = g()
    for a in A:
        dic[a].append(i)
for k in dic:
    dic[k] = dic[k][::-1]
ans = [0] * N
for C in g():
    if dic[C]:
        ans[dic[C].pop()] += 1
print(*ans)