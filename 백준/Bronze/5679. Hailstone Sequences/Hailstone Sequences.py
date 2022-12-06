while(n:=int(input())):
 a=[n]
 while n-1:n=[n//2,3*n+1][n%2];a+=[n]
 print(max(a))