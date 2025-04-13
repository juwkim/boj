n,*l=map(int,open(0).read().split())
c,w=l[:n],l[n:]
d=sorted(zip(w,c),key=lambda x:x[0]/x[1])
a,i=sum(c),-1
while i<n-1 and a>0:a-=2*d[i:=i+1][1]
print(sum(abs(x-y*d[i][0]/d[i][1])for x,y in zip(w,c)))