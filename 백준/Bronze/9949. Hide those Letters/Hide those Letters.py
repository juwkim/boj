i=1
while(s:=input())!='# #':
    s=(s+s.upper()).replace(' ', '')
    print('Case',i)
    for _ in[0]*int(input()):print(''.join(map(lambda x:'_'if x in s else x,input())))
    print('')
    i+=1