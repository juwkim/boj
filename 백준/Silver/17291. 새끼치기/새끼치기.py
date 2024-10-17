a,b,c,d=1,0,0,0
for i in range(int(input())-1):a,b,c,d=a+b+c+d,a,b,(i&1)*c
print(a+b+c+d)