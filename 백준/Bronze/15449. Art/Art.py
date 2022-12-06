from itertools import*
print(sum(a+b>c for a,b,c in combinations(sorted(map(int,input().split())),3)))