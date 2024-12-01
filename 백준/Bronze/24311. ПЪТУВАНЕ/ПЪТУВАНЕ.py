a,b,c,d,e,x,f=map(int,open(0).read().split())
print('%02d %02d'%divmod(60*(a-d)+b-e-c-10+~x*f,60))