import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product
n = int(input())
p, q = 0, 0
for a, b in product(g(), g()):
    p += a > b
    q += a < b
if p > q:
    print("first")
elif p < q:
    print("second")
else:
    print("tie")