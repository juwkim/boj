import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product
from collections import defaultdict

s = input()
dic = {}
for _ in range(int(input())):
    k, vs = input().split("=")
    v = vs.split(",")
    dic[k] = v

pos = defaultdict(list)
for i, c in enumerate(s):
    for k in dic:
        if c == k:
            pos[k].append(i)
            break

key = dic.keys()
buf = list(s)
for val in product(*dic.values()):
    for k, v in zip(key, val):
        for p in pos[k]:
            buf[p] = v
    print(*buf, sep="")