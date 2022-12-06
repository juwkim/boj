g=lambda:map(int,input().split())
a,b=g()
c,d=g()
N,t=input(),0
while a!=c or b!=d:
    t+=N in f'{a:#02d}{b:#02d}'
    b=(b+1)%60
    a+=b==0
t+=N in f'{a:#02d}{b:#02d}'
print(t)