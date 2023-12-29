import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import factorial

for _ in range(int(input())):
    S, *l = input().split()
    N, T, L = map(int, l)
    if S == 'O(N)':
        cnt = N
    elif S == 'O(N^2)':
        cnt = N * N
    elif S == 'O(N^3)':
        cnt = N * N * N
    elif S == 'O(2^N)':
        cnt = 2 ** N
    else: # S == 'O(N!)':
        cnt = factorial(N)
    cnt *= T
    if cnt > L * 10 ** 8:
        print('TLE!')
    else:
        print('May Pass.')