n,*l=map(int,open(0).read().split())
a,b=0,sum(l)
print(min(abs((a:=a+l[i])-(b:=b-l[i]))for i in range(n-1)))