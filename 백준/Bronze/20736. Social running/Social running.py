n,*l=map(int,open(0))
print(min(l[i-2]+l[i]for i in range(n)))