N,M,T,K=map(int,input().split())
n,q=(K+T-1)//T,N//M
print(M*min(q,n)*(2*K-T*(min(q,n)-1))//2+N%M*(q<n)*(K-T*q))