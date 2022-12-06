while n:=int(input()):
    s=0
    for _ in[0]*n:s+=(input()[s:]+' ').index(' ')
    print(s+1)