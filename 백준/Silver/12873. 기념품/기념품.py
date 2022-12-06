n=int(input())
a,p=[*range(1,1+n)],0
for i in range(1,n):a.pop(p:=(p+i**3-1)%len(a))
print(*a)