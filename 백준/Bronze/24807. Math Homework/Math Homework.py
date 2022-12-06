b,c,d,l=map(int,input().split())
f=1
for i in range(l//b+1):
    for j in range((l-b*i)//c+1):
        if (t:=l-i*b-j*c)%d==0:print(i,j,t//d);f=0
if f:print('impossible')