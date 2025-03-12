import sys
input = sys.stdin.readline
from itertools import permutations

for _ in range(int(input())):
    N = int(input())
    l = [*permutations(range(1, N + 1))]
    ans = l[len(l) // 3]
    print(*ans, sep='')