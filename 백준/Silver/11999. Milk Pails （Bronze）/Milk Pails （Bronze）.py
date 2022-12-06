X,Y,M=map(int,input().split())
print(max(M-(M-X*i)%Y for i in range(M//X+1)))