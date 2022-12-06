import math
P,N,R=map(int,open(0).read().split())
print(P//N if R==1 else int(math.log((R*P-P+N)/N,R)))