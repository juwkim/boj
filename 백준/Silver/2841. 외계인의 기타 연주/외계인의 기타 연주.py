import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

N, P = g()
dic = defaultdict(list)
ans = 0
for _ in range(N):
    x, y = g()
    while dic[x] and dic[x][-1] > y:
        dic[x].pop()
        ans += 1
    if dic[x] and dic[x][-1] == y:
        continue
    dic[x].append(y)
    ans += 1
print(ans)