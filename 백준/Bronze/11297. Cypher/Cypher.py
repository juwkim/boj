while(s:=input())[0]!='0':
    k=eval(s.replace(' ','+'))%25
    print(''.join(map(lambda s:[s,chr(97+(ord(s)-k-98)%26)]['`'<s<'{'],input())))