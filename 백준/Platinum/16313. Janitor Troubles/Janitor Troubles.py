a,b,c,d=map(int,input().split())
print((((p:=(a+b+c+d)/2)-a)*(p-b)*(p-c)*(p-d))**.5)