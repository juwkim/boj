X,Y,_,*l=map(int,open(0).read().split())
for A in l:print('YNEOS'[bool(A!=2 and(Y%A or(X-2)%A)and(((Y%A or(Y-2)%A)and(Y-1)%A)or(X-1)%A)and(X%A or(Y-2)%A))::2])