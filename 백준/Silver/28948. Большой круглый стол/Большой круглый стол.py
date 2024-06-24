n,k=map(int,input().split())
print(min((n//2,n)[n&1],k+1))