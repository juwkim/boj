from itertools import permutations, combinations

p = {int(''.join(p)) for p in permutations(input().split()) if p[0] != '0'}
print(sum(sum(l) in p for l in combinations(p, 3)))