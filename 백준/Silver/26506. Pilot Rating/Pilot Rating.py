n,*l=map(int,open(0))
l.sort()
print(min(l[i]+l[-i-1]for i in range(n>>1)))