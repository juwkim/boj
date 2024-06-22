n,a,*b=map(int,open(0).read().split())
print((a%3,1+(n==1 or b[0]&1))[a%3==2])