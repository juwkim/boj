a,b,c=input().split()
s=a+b+c
print(min((l for l in(s,s+a,s+b+a)if l==l[::-1]),key=int))