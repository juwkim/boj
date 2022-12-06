a='32123323322122122212111221'
A,B=map(lambda t:[*map(lambda s:int(a[ord(s)-65]),t)],[input(),input()])
s=[]
for x,y in zip(A,B):s+=[x,y]
while len(s)!=2:s=[sum(x)%10for x in zip(s,s[1:])]
print(*s,sep='')