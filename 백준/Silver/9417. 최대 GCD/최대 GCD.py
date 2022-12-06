import math as m
import itertools as i
for _ in[0]*int(input()):print(max(m.gcd(a,b)for a,b in i.combinations(map(int,input().split()),2)))