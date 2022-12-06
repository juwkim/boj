D,H,M=map(int,input().split())
t=1440*(D-11)+60*(H-11)+M-11
print([t,-1][t<0])