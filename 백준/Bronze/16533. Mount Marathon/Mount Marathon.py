input()
a=[*map(int,input().split())]
print(1+sum(x<y for x,y in zip(a,a[1:])))