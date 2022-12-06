J,R,*l=map(int,open(0).read().split())
print(max([[sum(l[i::J]),i+1]for i in range(J)])[1])