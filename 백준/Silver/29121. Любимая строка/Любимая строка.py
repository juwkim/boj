import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

n, m = map(int, input().split())
s = input()
words = defaultdict(list)
for i in range(1, m + 1):
    words[input()].append(i)
k = n // m
ans = [words[s[i:i+k]].pop() for i in range(0, n, k)]
print(*ans)