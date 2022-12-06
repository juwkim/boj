from itertools import*
g=lambda:map(int, input().split())
_,K=g()
print([*map(sum,combinations(g(),2))].count(K))