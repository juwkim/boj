A,B = 0, 0
while(s:=input())!='7':
    P=s.split()
    C,X=int(P[0]),P[1]
    if C==1:
        v = P[2]
        exec(f'{X}={v}')
    elif C == 2:
        eval(f'print({X})')
    else:
        v=int(eval('+*-/'[C-3].join(P[1:]))+(C==6)*(eval('*'.join(P[1:])) < 0))
        exec(f'{X}={v}')