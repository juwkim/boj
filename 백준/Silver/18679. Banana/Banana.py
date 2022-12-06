I,d=input,{}
for x,y in[I().split(' = ')for _ in[0]*int(I())]:d[x]=y
for _ in[0]*int(I()):I();print(*map(lambda x:d[x],I().split()))