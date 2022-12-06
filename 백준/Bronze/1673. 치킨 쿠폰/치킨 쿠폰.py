import sys
for l in sys.stdin:
    n,k=map(int,l.split())
    c,s=0,0
    while n:c+=n;n=(s:=s+n)//k;s%=k
    print(c)