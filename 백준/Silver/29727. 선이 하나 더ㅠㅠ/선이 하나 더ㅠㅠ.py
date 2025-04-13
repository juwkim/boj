n,x,y,X,Y=map(int,open(0).read().split())
d=max(0,(0,min(n,max(y,Y))-max(-1,min(y,Y)),min(n,max(x,X))-max(-1,min(x,X)))[(x==X)-(y==Y)])
a=n+1
print(a*(a*n*n//2+d*d-d)>>1)