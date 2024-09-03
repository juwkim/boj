n,r,k=map(int,input().split())
p=max(r,2*k-r)
print(r+max(p,n+(n-p&1)))