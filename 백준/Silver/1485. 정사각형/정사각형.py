import math
import itertools as i
for _ in range(int(input())):p=[[*map(int,input().split())]for _ in range(4)];print(+(len(set((math.dist(p[x],p[y])for x,y in i.combinations(range(4),2))))==2))