N,M=map(int,input().split())
print(sum(sorted(max(N-int(input().split()[0]),0)for _ in[0]*M)[:M-1]))