N,M,K=map(int,input().split())
b=int.bit_length
print(min(b(N),b(K)+M)-1)