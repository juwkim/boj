N,M=map(int,input().split())
a=1
for i in range(2,N+1):
 if(a:=a*i%M)==0:break
print(a)