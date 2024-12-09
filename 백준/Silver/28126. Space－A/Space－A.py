import sys
input = sys.stdin.readline
from collections import Counter

input()
ans, cnt = 0, Counter(input())
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans += cnt['R'] >= max(0, x - y, x - 1 - cnt['X']) and cnt['U'] >= max(0, y - x, y - 1 - cnt['X'])
print(ans)