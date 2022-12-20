K,N,*l=map(int,open(0).read().split())
a,b=0,2**31
g=lambda m:sum(i//m for i in l)
while a<=b:
    if g(m:=(a+b)//2)>N-1:a=m+1
    else:b=m-1
print(m-(N>g(m)))