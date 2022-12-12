import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

from collections import defaultdict
dic = defaultdict(list)
N, K = g()
colors = []
for _ in range(N):
    num, color = g()
    dic[color].append(num)
    colors.append(color)
for color in dic:
    dic[color].sort(reverse=True)

ans, cur = 'Y', 0
for color in colors:
    num = dic[color].pop()
    if cur > num:
        ans = 'N'
        break
    cur = num
print(ans)