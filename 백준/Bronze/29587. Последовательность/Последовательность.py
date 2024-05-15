from itertools import pairwise

n, *a = map(int, open(0).read().split())
if all(p < q for p, q in pairwise(a)):
    print(0)
else:
    print(n)
    print(*range(1, n + 1))