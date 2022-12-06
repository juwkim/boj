_,*l=open(0).read().split()
for a in zip(*l):print(1==len({*a})and a[0]or'?',end='')