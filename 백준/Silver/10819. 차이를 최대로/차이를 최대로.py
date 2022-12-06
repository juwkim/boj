g = lambda: [*map(int, input().split())]
from itertools import permutations
ans = 0
N = int(input())
for l in permutations(g(), N):
    num = sum(abs(a - b) for a, b in zip(l, l[1:]))
    ans = max(ans, num)
print(ans)