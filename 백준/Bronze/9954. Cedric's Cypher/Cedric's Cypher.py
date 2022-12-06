while (s:=input())!='#':
    a=ord(s[-1])-65
    b=[*map(lambda x:x.isupper()-x.islower(),s)]
    print(''.join([b[i]and chr((ord(s[i])+16*b[i]-a-81)%26+81-16*b[i])or s[i]for i in range(len(s)-1)]))