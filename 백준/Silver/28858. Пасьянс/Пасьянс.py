from itertools import pairwise

n, *l = map(int, open(0).read().split())
print(sum((a ^ b) & 1 for a, b in pairwise(sorted(l))) + 1)