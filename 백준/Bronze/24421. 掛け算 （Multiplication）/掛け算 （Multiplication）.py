from itertools import*
input()
print(sum(x*y==z for x,y,z in combinations(map(int,input().split()),3)))