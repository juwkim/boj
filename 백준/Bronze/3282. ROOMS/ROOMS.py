N,G,*l=map(int,open(0).read().split())
r=[0]*N
for c in l:
 while c:
  try:a=min(c,2);r[r.index(0)]=a;c-=a
  except:r[r.index(1)]=2;c-=1
print(*r)