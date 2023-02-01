for _ in range(int(input())):
    word = input()
    buf = []
    converted = False
    for i in range(len(word)):
        
        if word[i] != 'o':
            converted = False
        
        if i != 0 and word[i] == 's' and (i == len(word) - 1 or word[i+1] != 'h'):
            buf.append('th')
            continue
        
        if i == 0 and word[i] == 'e':
            buf.append('ae')
            continue
        
        if i == 0 and word[i] == 'E':
            buf.append('Ae')
            continue
        
        if not converted and word[i] == 'o' and buf and buf[-1] == 'o':
            buf[-1] = 'ou'
            converted = True
            continue

        if not converted and word[i] == 'o' and buf and buf[-1] == 'O':
            buf[-1] = 'Ou'
            converted = True
            continue
        
        buf.append(word[i])

    print(*buf, sep='')