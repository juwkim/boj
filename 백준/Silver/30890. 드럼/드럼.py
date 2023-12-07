import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import lcm

X, Y = g()
l = lcm(X, Y)
a, b = l // X, l // Y
ans = []
for i in range(1, l + 1):
    p, q = i % a, i % b
    if p == 0 and q == 0:
        ans.append('3')
    elif p == 0:
        ans.append('1')
    elif q == 0:
        ans.append('2')
print(*ans, sep='')