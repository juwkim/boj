for t in range(1, 1 + int(input())):
    
    input()
    txt = input()
    if len(txt) == 1:
        ans = 'IMPOSSIBLE'
    else:
        buf = list(set(txt))
        for c in map(chr, range(65, 91)):
            if c not in buf:
                buf.append(c)
        
        buf[0], buf[1] = buf[1], buf[0]
        ans = ''.join(buf)

    print(f'Case #{t}: {ans}')