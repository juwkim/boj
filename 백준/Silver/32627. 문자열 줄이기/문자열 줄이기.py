from collections import Counter
from string import ascii_lowercase

N, M = map(int, input().split())
cnt = Counter(S := input())
d = {}
for c in ascii_lowercase:
    t = min(M, cnt[c])
    d[c] = t
    M -= t
    if M == 0:
        break
for c in S:
    if d.get(c, 0):
        d[c] -= 1
    else:
        print(c, end='')