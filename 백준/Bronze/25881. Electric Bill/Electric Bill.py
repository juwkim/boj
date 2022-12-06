a,b=map(int,input().split())
exec("n=int(input());print(n,max(a*n,b*n+(a-b)*1000));"*int(input()))