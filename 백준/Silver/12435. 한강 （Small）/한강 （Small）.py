import sys
input = sys.stdin.readline
from math import isqrt
from collections import defaultdict
num = 1000000
dic = defaultdict(list)
l = [[0, 0] for _ in range(num + 1)]
for i in range(4, num + 1):
    last, cnt = 0, 0
    for j in range(2, isqrt(i) + 1):
        k, r = divmod(i, j)
        if r == 0:
            if last == 0:
                last = j
            cnt += 1
            if j != k:
                cnt += 1
    if last:
        dic[cnt].append((i, last))
        l[i] = [last, cnt]

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    ans, cnt = 0, l[N][1]
    for i, last in dic[cnt]:
        if i >= N:
            break
        if last >= M:
            ans += 1
    print(f"Case #{tc}: {ans}")