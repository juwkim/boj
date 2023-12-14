import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

'''
one set: K ~ K + (K - 2) = K ~ 2 * K - 2
duce: (K + 1) + (K - 1) = 2 * K, 2 * K + 2, 2 * K + 4, ...
S sets: S * K ~
'''

K, S, N = g()

if S == 1:
    if (N >= K and N <= 2 * K - 2) or (N >= 2 * K and N % 2 == 0):
        print('YES')
    else:
        print('NO')
else:
    if N >= S * K:
        print('YES')
    else:
        print('NO')