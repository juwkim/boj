N,M=map(int,open(0))
print(30+([M,max(N,M)][N&1]-1)//N*10)