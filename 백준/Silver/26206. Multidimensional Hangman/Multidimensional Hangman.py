import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
import string
N, C = map(int, input().split())
cnt = Counter()
for _ in range(N):
    s = input()
    i = s.find('*')
    s = [*s]
    for c in string.ascii_lowercase:
        s[i] = c
        cnt["".join(s)] += 1
k, v = min(cnt.items(), key=lambda x: (-x[1], x[0]))
print(k, v)