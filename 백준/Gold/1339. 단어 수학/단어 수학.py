import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

wei = [1]
for _ in range(7):
    wei.append(wei[-1] * 10)
dic = defaultdict(int)
N = int(input())
words = [input() for _ in range(N)]
for word in words:
    for i, c in enumerate(word[::-1]):
        dic[c] += wei[i]
ans = 0
num = 9
for k in sorted(dic, key=lambda k: -dic[k]):
    ans += num * dic[k]
    num -= 1
print(ans)