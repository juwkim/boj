N,C,W,*L=map(int,open(0).read().split())
print(max(sum(max(0,t//i*i*W-(t-1)//i*C)for t in L)for i in range(1,10001)))