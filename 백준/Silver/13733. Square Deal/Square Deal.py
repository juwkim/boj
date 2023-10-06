import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product
a = g()
b = g()
c = g()

def solve():
    for i, j in product(range(2), repeat=2):
        if b[i] == c[j]:
            H, W = b[i], b[1-i] + c[1-j]
            break
    else:
        return 'NO'
    d = [H, W]
    for i, j in product(range(2), repeat=2):
        if a[i] == d[j]:
            H, W = a[i], a[1-i] + d[1-j]
            break
    else:
        return 'NO'
    if H == W:
        return 'YES'
    else:
        return 'NO'

print(solve())