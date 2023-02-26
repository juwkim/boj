x,y,z,c,d,n=map(int,open(0).read().split())
p,q=x-c,d-x
print((p>=0)*(q>=0)*((y*y<=4*z*p)or((-y<=2*n*p)*(p*n*n+y*n>=-z)))*((y*y<=-4*z*q)or((y<=2*n*q)*(q*n*n-y*n>=z))))