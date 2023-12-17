import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

input()
cnt = Counter(input())
l = max(cnt.values())

ans = [k for k, v in cnt.items() if v == l]
if len(ans) == 3:
    print('SCU')
else:
    print(*sorted(ans, key=lambda x: "BSA".index(x)), sep="")