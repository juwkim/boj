v=[int(input())]
while(s:=input())!='#':v+=[(1+(v[-1]+int(s[1])*(-1)**(s[0]=='A')-1)%8)]
print(*v,'reject'if len(v)<5 or len(v)-len(set(v))else'')