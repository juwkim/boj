s=[*map(int,input())]
print('READY'if sum(s[:(k:=len(s)//2)])-sum(s[k:])else'LUCKY')