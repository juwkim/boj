N,C,W,*L=map(int,open(0).read().split())
print(max(sum(max(0,t//i*i*W-(t//i-(t%i==0))*C)for t in L)for i in range(1,10001)))