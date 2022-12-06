x,y,z,c,d,n=map(int,open(0).read().split())
p=x-c
a = (p>=0)*((y*y<=4*z*p)or((-y<=2*n*p)*(p*n*n+y*n>=-z)))
p=d-x
b = (p>=0)*((y*y<=-4*z*p)or((y<=2*n*p)*(p*n*n-y*n>=z)))
print(a*b)