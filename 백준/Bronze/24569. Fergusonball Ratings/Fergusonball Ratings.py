n,*l=map(int,open(0).read().split())
a=sum(40<5*l[2*i]-3*l[2*i+1]for i in range(n))
print(str(a)+' +'[a==n])