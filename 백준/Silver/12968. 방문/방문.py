R,C,K=map(int,input().split())
print(1-(R&1)*(C&1)*(K!=1))