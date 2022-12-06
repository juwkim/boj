r = '*?/+!'
while (word:= input()) != '#':
    buf = set()
    dic = dict()
    cnt = 0
    for c in word:
        l_c = c.lower()
        if dic.get(l_c):
            print(dic[l_c], end='')
        elif l_c in buf:
            dic[l_c] = r[cnt]
            cnt += 1
            print(dic[l_c], end='')
        else:
            buf.add(l_c)
            print(c, end='')
    print()