_,*l=open(0).read().split()
a=len(l[0])
print(max(10**(a-1),int(max(l))),10**a-1)