import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import isqrt

def solve(S, P):
    if P & 1:
        return -1
    a, b, c = 1, -P // 2, S
    d = b ** 2 - 4 * a * c
    if d < 0 or isqrt(d) ** 2 != d:
        return -1 

    q1, r1 = divmod(-b + isqrt(d), 2 * a)
    q2, r2 = divmod(-b - isqrt(d), 2 * a)
    if r1 or r2:
        return -1 
    return str(q1) + ' ' + str(q2)

print(solve(*g()))