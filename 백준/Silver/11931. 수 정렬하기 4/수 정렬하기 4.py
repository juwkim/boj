n,*l=open(0).read().split()
l.sort(reverse=True,key=int)
print(*l)