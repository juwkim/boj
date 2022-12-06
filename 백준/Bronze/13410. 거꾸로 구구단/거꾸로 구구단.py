N,K=map(int,input().split())
print(max(int(str(N+N*i)[::-1])for i in range(K)))