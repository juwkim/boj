from collections import*
I=input
x,y=I(),I()
a,b=map(Counter,[x,y])
print(len(x+y)-2*sum(min(a[s],b[s])for s in a if s in b))