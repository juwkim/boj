res = set()
while (s:= input()) != '##':
    res.add(s)
while (s:= input()) != '#':
    for word in s.split():
        if len(word) >= 4 and word[0] + word[3] in res:
            print(word[0] + '**' + word[3:], end=' ')
        else:
            print(word, end=' ')
    print()