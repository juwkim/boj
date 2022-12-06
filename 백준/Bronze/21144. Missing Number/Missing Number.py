n,s=open(0)
t=0
for i in map(str,range(1,int(n)+1)):
 p=t+len(i)
 if s[t:p]!=i:print(i);break
 t=p