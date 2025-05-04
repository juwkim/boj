import sys
input = sys.stdin.readline
from collections import Counter, defaultdict

M = int(input())
dic = defaultdict(Counter)
for _ in range(M):
    user, *words = input().split()
    dic[user].update(Counter(words))
buf = []
keys, *_ = dic.values()
for k in keys:
    if all(b[k] for b in dic.values()):
        buf.append((-sum(b[k] for b in dic.values()), k))
if buf:
    for v, k in sorted(buf):
        print(k)
else:
    print("ALL CLEAR")