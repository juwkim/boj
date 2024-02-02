N,k=map(int, input().split())
p=0
for i in range(N-1):p+=p//(k-1)+1
print(p)