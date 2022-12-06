n,*l=map(int,open(0))
print(100+max(sum(l[:i])for i in range(n+1)))