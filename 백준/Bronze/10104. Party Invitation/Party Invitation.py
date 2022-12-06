K,m=map(int,[input(),input()])
f=[*range(1,K+1)]
for _ in[0]*m:
    t=(r:=int(input())-1)
    while t<len(f):
        f.pop(t)
        t+=r
print(*f)