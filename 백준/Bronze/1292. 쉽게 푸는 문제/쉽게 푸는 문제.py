A,B=map(int,input().split())
g=lambda n:(t:=int(((8*n+1)**.5+1)/2))*(6*n-t*t+1)//6
print(g(B)-g(A-1))