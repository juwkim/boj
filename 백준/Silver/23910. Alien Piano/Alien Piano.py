import sys
input = sys.stdin.readline
from itertools import pairwise

for tc in range(1, 1 + int(input())):
    input()
    ans, s = 0, (1, 1, 1, 1)
    for A, B in pairwise(map(int, input().split())):
        if A == B:
            continue
        if A < B:
            if s[0]:   s = 0, 1, 1, 1
            elif s[1]: s = 0, 0, 1, 1
            elif s[2]: s = 0, 0, 0, 1
            else:      s = 1, 1, 1, 1; ans += 1
        else:
            if s[3]:   s = 1, 1, 1, 0
            elif s[2]: s = 1, 1, 0, 0
            elif s[1]: s = 1, 0, 0, 0
            else:      s = 1, 1, 1, 1; ans += 1
    print(f"Case #{tc}: {ans}")