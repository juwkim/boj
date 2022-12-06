g=lambda s,i:map(int,s.split(i))
for _ in[0]*int(input()):
    if'.'in(s:=input()):d,m,y=g(s,'.')
    else:m,d,y=g(s,'/')
    print(f'{d:#02d}.{m:#02d}.{y:#04d} {m:#02d}/{d:#02d}/{y:#04d}')