for _ in range(int(input())):
    buf = [' ']
    s = input()
    for i in range(len(s)):
        if s[i] in ':-':
            if buf[-1] != ' ':
                buf.append(' ')
            buf.append(s[i])
            if i != len(s) - 1 and s[i+1] != ' ':
                buf.append(' ')
        else:
            buf.append(s[i])
    print(*buf[1:], sep='')