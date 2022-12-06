n,k,x,y,*l=map(int,open(0).read().split())
print(sum((a-x)**2+(b-y)**2>k*k for a,b in zip(l[::2],l[1::2])))