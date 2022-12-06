N,*l=map(int,open(0).read().split())
print(sum(min(abs(s-t),360-abs(s-t))for s,t in zip(l,l[1:])))