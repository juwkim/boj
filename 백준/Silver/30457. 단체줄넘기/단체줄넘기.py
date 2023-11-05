import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter
N = int(input())
ans = sum(min(2, v) for k, v in Counter(g()).items())
print(ans)