import sys
from itertools import pairwise
input = lambda: sys.stdin.readline().strip()

while (t:=input()) != '0':
    n, *nums = map(int, t.split())
    seq = [b - a for a, b in pairwise(nums)]
    s = n - 1
    ans = s
    for i in range(1, s):
        a = seq[:i]
        if any(a != seq[j:j+i] for j in range(i, s - i + 1, i)):
            continue
        r = s % i
        if r and a[:r] != seq[-r:]:
            continue
        ans = i
        break
    print(ans)