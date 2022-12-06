N=int(input())
l,t,o=[-1]*N,0,0
for _ in range(int(input())):
 c=int(input())
 for i in range(c-1,N,c):l[i]*=-1;o+=l[i]
 if (t:=max(t,o))==N:break
print(t)