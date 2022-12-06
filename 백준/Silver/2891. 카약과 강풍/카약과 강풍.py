g=lambda:map(int,input().split())
g()
p,o={*g()},{*g()}
b,c=p-o,0
o-=p
for t in b:
 if t-1 in o:o.remove(t-1)
 elif t+1 in o:o.remove(t+1)
 else:c+=1
print(c)