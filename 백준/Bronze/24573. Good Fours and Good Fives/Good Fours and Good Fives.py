N=int(input())
print(sum(((N-4*i)%5==0)for i in range(0,N//4+1)))