from itertools import permutations, combinations

perms = {int(''.join(p)) for p in permutations(input().split()) if p[0] != '0'}
print(sum(sum(l) in perms for l in combinations(perms, 3)))