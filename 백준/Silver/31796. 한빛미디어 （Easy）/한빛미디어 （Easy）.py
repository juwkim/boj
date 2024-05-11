n,*p=map(int,open(0).read().split())
p.sort()
a,b=0,0
for i in p:
 if i>=b*2:b=i;a+=1
print(a)