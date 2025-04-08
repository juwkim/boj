import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())
from itertools import product

H1, W1 = g()
a = [input() for _ in range(H1)]
H2, W2 = g()
b = [input() for _ in range(H2)]
coins = sum(l.count('O') for l in a)
max_match, visited = 0, set()
for i, j, k, l in product(range(H1), range(W1), range(H2), range(W2)):
    d1, d2 = k - i, l - j
    if (d1, d2) in visited:
        continue
    visited.add((d1, d2))
    match = 0
    for s in range(H1):
        for t in range(W1):
            if a[s][t] == 'O' and 0 <= s + d1 < H2 and 0 <= t + d2 < W2 and b[s + d1][t + d2] == 'O':
                match += 1
    max_match = max(max_match, match)
print(coins - max_match)