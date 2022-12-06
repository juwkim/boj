g=lambda:map(int, input().split())
_,M=g()
d,b=0,0
for _ in[0]*M:
    B,*n=g()
    if sum(n)<=B:d+=n[0]
    c=1
    while c<=10000and c+sum(n[1:])<=B:c*=10
    b+=c//10
print(b-d)