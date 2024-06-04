g = lambda: [*map(int, input().split())]
from itertools import permutations, pairwise

n = int(input())
p, a = g(), g()
print(sum(all(a + b <= c for (a, b), c in zip(pairwise(l), a)) for l in permutations(p)))