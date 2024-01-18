import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import inf

N = int(input())
e, o = -1, -1
even_d, odd_d = inf, inf
for num in sorted(g()):
    if num & 1:
        if e != -1:
            odd_d = min(odd_d, num - e)
        if o != -1:
            even_d = min(even_d, num - o)
        o = num
    else:
        if o != -1:
            odd_d = min(odd_d, num - o)
        if e != -1:
            even_d = min(even_d, num - e)
        e = num
if even_d == inf:
    even_d = -1
if odd_d == inf:
    odd_d = -1
print(even_d, odd_d)