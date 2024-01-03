I=input
for _ in " "*int(I()):
 I()
 m,c=max(n:=[*map(int,I().split())]),[0]*(p:=1<<20)
 for q in n:c[q]+=1
 d=c[:]
 for i in range(20):
  for s in range(p):
   if s&(1<<i):d[s]+=d[s^(1<<i)]
 print(sum(d[i]*c[i]for i in range(p)))