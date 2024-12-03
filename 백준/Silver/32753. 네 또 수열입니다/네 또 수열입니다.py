N,K=map(int,input().split())
p=print
if N==1:p(*[1]*(N*K))
elif(N,K)==(2,1):p(1,2)
else:p(-1)