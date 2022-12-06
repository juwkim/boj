N,*l=map(int, open(0).read().split()) 
a=0
for i in range(N-2,-1,-1):
 n=l[i+1]-1
 if l[i]>n:
  a+=l[i]-n
  l[i]=n
print(a)