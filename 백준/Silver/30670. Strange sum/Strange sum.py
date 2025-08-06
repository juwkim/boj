import sys
input = sys.stdin.readline
from collections import defaultdict

def solve(arr):
    total, px = 0, 0
    for i, x in enumerate(sorted(arr)):
        total += x * i - px
        px += x
    return total

n, m = map(int, input().split())
rows = defaultdict(list)
cols = defaultdict(list)
for r in range(n):
    for c, color in enumerate(map(int, input().split())):
        rows[color].append(r)
        cols[color].append(c)
print(sum(solve(rows[color]) + solve(cols[color]) for color in rows))