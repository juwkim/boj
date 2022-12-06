x,y,a,b=open(0).read().split()
i=int
if x=='AD':
 if a=='AD':v=abs(i(y)-i(b))
 else:v=i(a)+i(y)-1
else:
 if a=='AD':v=i(b)+i(x)-1
 else:v=abs(i(x)-i(a))
print(v)