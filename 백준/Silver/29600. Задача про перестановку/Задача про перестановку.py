import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import permutations, pairwise

n, k = map(int, input().split())
cnt = 0
for l in permutations(range(1, n + 1)):
    if all(a + b != 3 for a, b in pairwise(l)):
        cnt += 1
        if cnt == k:
            print(*l)
            break