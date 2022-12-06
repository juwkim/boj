while (s:=input()) != 'END':
    k = s.replace(' ', '')
    if list(k) == sorted(list(set(k)), key=s.index):
        print(s)