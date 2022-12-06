import itertools as i
for s in i.combinations(map(int,open(0)),7):
    if sum(s)==100:print(*sorted(s));break