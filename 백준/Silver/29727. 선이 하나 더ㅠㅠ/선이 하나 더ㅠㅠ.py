n,x,y,X,Y=map(int,open(0).read().split())
d=0
if x==X:d=min(n,max(y,Y))-max(-1,min(y,Y))
elif y==Y:d=min(n,max(x,X))-max(-1,min(x,X))
a,d=n+1,max(0,d)
print(a*(a*n*n//2+d*d-d)>>1)