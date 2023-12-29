import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import factorial

for l in map(str.rstrip, sys.stdin):
    s, num = l.split()
    num = int(num)
    if factorial(len(s)) < num:
        ans = "No permutation"
    else:
        ans = ""
        s = sorted(s)
        while s:
            n = factorial(len(s) - 1)
            idx = (num - 1) // n
            ans += s.pop(idx)
            num -= idx * n
    print(f"{l} = {ans}")