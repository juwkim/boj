h=lambda p:''.join(map(lambda x:str(x).rjust(3),p))
while(s:=input())!='0':
    n,*a=map(int,s.split())
    b=sorted([*range(n)],key=lambda x:a[n-x-1])
    c=[*map(lambda x:n-x-1,a)][::-1]
    d=sorted([*range(n)],key=lambda x:-a[x])
    print('\n'.join(map(h,[a,b,c,d,*map(reversed,[c,b,a,d])]))+'\n')