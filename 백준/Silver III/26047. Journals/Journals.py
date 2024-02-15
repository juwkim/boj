from itertools import pairwise
print((sum(a==b for a,b in pairwise(input()))+1)//2)