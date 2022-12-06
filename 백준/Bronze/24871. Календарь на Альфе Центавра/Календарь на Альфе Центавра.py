d,m,w,i,j,k=map(int,open(0).read().split())
print(chr(97+(d*m*(k-1)+d*(j-1)+i-1)%w))