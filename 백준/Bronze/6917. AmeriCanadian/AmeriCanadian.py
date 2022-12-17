while (s:= input()) != 'quit!':
    if len(s) >= 4 and s[-2:] == 'or' and s[-3] not in 'aeiouy':
        s = s[:-1] + 'ur'
    print(s)