a,b,c=sorted(map(int,input().split()))
print(max(a+b*c, a*b+c, a*c+b))