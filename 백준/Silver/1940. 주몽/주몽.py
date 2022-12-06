g = lambda: [*map(int, input().split())]

from collections import defaultdict
N = int(input())
M = int(input())

dic = defaultdict(int)
ans = 0
for num in g():
    if dic[M - num] > 0:
        ans += 1
        dic[M - num] -= 1
    else:
        dic[num] += 1
print(ans)