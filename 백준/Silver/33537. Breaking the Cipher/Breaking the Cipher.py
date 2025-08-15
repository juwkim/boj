p,q,e,C=map(int,open(0).read().split())
print(pow(C,pow(e,-1,p*q-p-q+1),p*q))