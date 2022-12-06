for _ in[0]*int(input()):
    t=''
    while(s:=input())!='':t+=s
    x=round((1-t.count('#')/len(t))*100,1)
    if x==int(x):x=int(x)
    print(f'Efficiency ratio is {x}%.')