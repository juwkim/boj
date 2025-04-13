g=lambda:[*map(int,input().split())]
n=int(input())
c=g();w=g()
d=sorted(zip(w,c),key=lambda x:x[0]/x[1])
a,i=sum(c),-1
while i<n-1 and a>0:a-=2*d[i:=i+1][1]
r=d[i][0]/d[i][1]
print(sum(abs(x-r*y)for x,y in zip(w,c)))