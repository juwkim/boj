while(s:=input())!='#':
    k=(11-sum((i+2)*int(x)for i,x in enumerate(s[::-1]))%11)%11
    if k==10:k='Rejected'
    print(f'{s} -> {k}')