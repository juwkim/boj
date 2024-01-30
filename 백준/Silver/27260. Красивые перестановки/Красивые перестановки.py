import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import permutations

n, k = g()
ans = 0
for l in permutations(range(1, n + 1)):
    if sum(a * b for a, b in zip(l, l[1:])) % k == 0:
        ans += 1
print(ans)