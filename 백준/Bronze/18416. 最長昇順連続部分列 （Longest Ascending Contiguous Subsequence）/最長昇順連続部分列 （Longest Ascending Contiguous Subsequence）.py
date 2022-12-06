N=int(input())
t,j=[*map(int,input().split())],N
while all(t[i:i+j]!=sorted(t[i:i+j])for i in range(N-j+1)):j-=1
print(j)