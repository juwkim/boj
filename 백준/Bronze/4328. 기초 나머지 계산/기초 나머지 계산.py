while(s:=input())!='0':
    b,p,m=s.split()
    b,k=int(b),''
    n=int(p,b)%int(m,b)
    while n:k=str(n%b)+k;n//=b
    print(k if k else 0)