import sys
from itertools import pairwise
input = sys.stdin.readline

while True:
    n, *nums = map(int, input().split())
    if n == 0:
        break
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