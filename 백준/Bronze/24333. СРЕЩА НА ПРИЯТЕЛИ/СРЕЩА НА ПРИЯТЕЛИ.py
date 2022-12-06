a,b,c,d,k=map(int,input().split())
a,b=min(b,d),max(a,c)
print(max(a-b+1,0)-(b<=k<=a))