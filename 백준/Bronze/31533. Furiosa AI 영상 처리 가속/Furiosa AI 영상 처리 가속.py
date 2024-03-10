a=int(input())
m,n=sorted(map(int,input().split()))
print(min(2*m/a,max(m,n/a)))