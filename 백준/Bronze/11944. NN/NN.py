import itertools as i
N,M=input().split()
for _,x in zip(range(min(len(N)*int(N),int(M))),i.cycle(N)):print(x,end='')