N,K=map(int,input().split())
print(["Your wish is granted!","You will become a flying monkey!"][K<len(bin(N))-3+(N&N-1!=0)])