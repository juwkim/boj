n,k=map(int,input().split())
n-=1;k-=1
print((-1,n//k)[n%k==0]if k else(-1,0)[n==0])