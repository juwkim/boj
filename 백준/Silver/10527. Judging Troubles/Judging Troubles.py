import sys
input = lambda: sys.stdin.readline().rstrip('\n')

from collections import Counter
n = int(input())
a = Counter([input() for _ in range(n)])
b = Counter([input() for _ in range(n)])
ans = sum((a & b).values())
print(ans)