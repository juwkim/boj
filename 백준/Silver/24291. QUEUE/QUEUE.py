N,K=map(int,input().split())
while N-K>4:
 q,r=divmod((K+1)*N-K+1,K+2)
 if r==0:N=q
 elif r<max(2,2*K+7-N):break
 else:N=q+1
print(N)