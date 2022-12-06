m,n='LIE','TRUTH'
_,a,*l=open(0).read().split()
print(l.count(m)%2 and{m:n,n:m}[a]or a)