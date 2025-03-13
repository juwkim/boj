import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
from itertools import permutations

while (s:=input()) != '#':
    cnt = Counter(s.split(','))
    while (s:=input()) != '#':
        for i in s.split(','):
            cnt[i] += 1
    ans, Max = None, 0
    for l in permutations("PGASN"):
        cur = 0
        for a, b in zip("roygb", l):
            cur += cnt[f"{a}/{b}"]
        if cur > Max:
            ans, Max = l, cur
    print(",".join(f"{a}/{b}" for a, b in zip("roygb", ans)))