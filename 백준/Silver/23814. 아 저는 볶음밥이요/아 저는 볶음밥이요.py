D,N,M,K=map(int,open(0).read().split())
a,b=D-N%D,D-M%D
print(max((K//D,K),(1+(K-a)//D,K-a),(1+(K-b)//D,K-b),(2+(K-a-b)//D,K-a-b))[1])