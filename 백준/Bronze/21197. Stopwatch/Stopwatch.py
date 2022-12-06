n,*l=map(int,open(0))
print('still running'if n%2 else sum(l[i+1]-l[i]for i in range(0,n,2)))