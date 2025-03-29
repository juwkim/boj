v,x,y,a,b=map(int,input().split())
f=lambda p,q:((2*q/p)**.5,v/p/2+q/v)[v*v<2*p*q]
print(f(b,x)+f(a,y))