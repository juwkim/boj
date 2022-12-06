x,y,z,c,n=map(int,open(0).read().split())
p=x-c
print(int((p>=0)*((y*y<=4*z*p)or((-y<=2*n*p)*(p*n*n+y*n>=-z)))))