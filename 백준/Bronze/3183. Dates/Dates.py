from datetime import*
while(s:=input())!='0 0 0':
    try:date(*map(int,s.split()[::-1]));s='V'
    except:s='Inv'
    print(s+'alid')