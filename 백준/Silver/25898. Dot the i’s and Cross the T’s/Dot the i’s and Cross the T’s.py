import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations
from math import dist

def same(a, b):
    return abs(a - b) <= 1e-6

def is_middle(a, b, m):
    return same(a[0] + b[0], 2 * m[0]) and same(a[1] + b[1], 2 * m[1])

for tc in range(1, 1 + int(input())):
    p = int(input())
    nums = [[*map(float, input().split())] for _ in range(p)]
    ans = 0
    for A, B, C, M in permutations(nums, 4):
        if is_middle(A, B, M) and same(dist(A, B), dist(C, M)):
            MA = (A[0] - M[0], A[1] - M[1])
            MC = (C[0] - M[0], C[1] - M[1])
            if same(MA[0] * MC[0] + MA[1] * MC[1], 0):
                ans += 1
    print(f'Set #{tc}: {ans // 2}')
    print()