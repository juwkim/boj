while True:
    try:
        input()
        dic = {}
        while (s:= input()) != 'END':
            name, a, b = s.split()
            dic[name] = int(b) - int(a)
        print(*sorted(dic.keys(), key=lambda x: -dic[x]), sep='\n')
        print()
    except:
        break