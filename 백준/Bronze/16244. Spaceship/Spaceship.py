n,*l=map(int,open(0).read().split())
l.remove(p:=(sum(l)//2))
print(*l,p)