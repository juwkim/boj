n,t,*l=map(int,open(0).read().split())
if t&1:
    print(*l[::-1])
else:
    print(*l)