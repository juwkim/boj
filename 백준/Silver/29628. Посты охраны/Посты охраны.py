a,b,c=sorted(map(int,input().split()))
print(c/(4-max(0,(a*a+b*b-c*c)/a/b)**2)**.5)