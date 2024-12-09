N,b,*R=map(int,open(0).read().split())
a=0
for p in R:a,b=b,min(a,b)+p
print(min(a,b))