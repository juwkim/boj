from itertools import*
o=[0]*(n:=int(input()))
for c in combinations([input()+' '+str(i)for i in range(n)],2):
    a,b=map(lambda s:[*map(int,s.split())],c)
    if(a[0]-b[0])**2+(a[1]-b[1])**2<(a[2]+b[2])**2:
        o[a[3]]+=1
        o[b[3]]+=1
print(*o,sep='\n')