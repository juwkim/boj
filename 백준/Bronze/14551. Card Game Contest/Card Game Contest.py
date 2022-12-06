N,M=map(int,input().split())
S=1
for _ in range(N):S=S*max(int(input()),1)%M
print(S%M)