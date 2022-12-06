T,D,M,*l=map(int,open(0).read().split())
print('NY'[any(b-a>=T for(a,b)in zip([0]+l,l+[D]))])