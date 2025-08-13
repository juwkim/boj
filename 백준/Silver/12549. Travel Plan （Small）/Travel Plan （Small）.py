import sys
input = sys.stdin.readline
from itertools import permutations, pairwise

for tc in range(1, int(input()) + 1):
    N = int(input())
    _, *X = map(int, input().split())
    F = int(input())
    ans = 0
    for p in permutations(X):
        cur = abs(p[0]) + abs(p[-1]) + sum(abs(x - y) for x, y in pairwise(p))
        if ans < cur <= F:
            ans = cur
    print(f"Case #{tc}: {ans if ans else 'NO SOLUTION'}")