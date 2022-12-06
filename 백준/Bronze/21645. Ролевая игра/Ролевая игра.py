n,m,k=map(int,input().split())
print(n*min(m,m//k+k-1))