a,b,c=sorted(map(int,input().split()))
print(a+b+min(c,a+b-1))