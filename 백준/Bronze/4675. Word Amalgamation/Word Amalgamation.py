from collections import Counter
dic = {}
while(s:=input())!='XXXXXX':
    dic[s] = Counter(s)
while(s:=input())!='XXXXXX':
    words = sorted([k for k in dic if dic[k] == Counter(s)])
    if words:
        print(*words, sep='\n')
    else:
        print('NOT A VALID WORD')
    print('******')