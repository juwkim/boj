n=int(input())
a=(n-1)//2*n+[0,-2*n//3][n%3==0]
print(a)