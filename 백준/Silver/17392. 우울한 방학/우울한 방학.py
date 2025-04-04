N,M,*H=map(int,open(0).read().split())
q,r=divmod(M-N-sum(H),N+1)
print(max(0,r*(q+1)**2+(N+1)*q*(q+1)*(2*q+1)//6))