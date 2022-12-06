g=lambda:[*map(int,input().split())]
c=[g()for _ in[0]*16]
while -1 not in(s:=g()):print(f'({",".join(map(str,s))}) maps to ({",".join(map(str,min(c,key=lambda x:sum((x-y)**2 for x,y in zip(s,x)))))})')