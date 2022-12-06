M,*l=map(int,open(0).read().split())
print(min(l,key=lambda x:(-l.count(x),x)))