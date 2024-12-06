import sys
input = sys.stdin.readline
from itertools import permutations

names = 'Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue'
l = []
N = int(input())
for _ in range(N):
    a, *_, b = input().split()
    l.append((a, b))
for p in permutations(names):
    idx = {name: i for i, name in enumerate(p)}
    if all(abs(idx[a] - idx[b]) == 1 for a, b in l):
        print(*p, sep='\n')
        break