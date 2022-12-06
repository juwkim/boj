n,s=int(input()),[i for i in input()]
for i in range(n):
    if s[n-1-i]!='?':s[i]=s[n-1-i]
print(''.join(s).replace('?','a'))