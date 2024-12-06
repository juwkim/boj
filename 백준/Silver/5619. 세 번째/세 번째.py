from itertools import permutations

n, *a = map(int, open(0))
a.sort()
l = []
for p, q in permutations(a[:4], 2):
    l.append(int(f"{p}{q}"))
l.sort()
print(l[2])