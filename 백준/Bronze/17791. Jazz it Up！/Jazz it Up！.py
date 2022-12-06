n,m=int(input()),2
while not all(n*m%s**2 for s in range(2,int((n*m)**.5)+1)):m+=1
print(m)