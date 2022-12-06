while True:
    s = input().replace(')', ' ) ').replace('(', ' ( ').split()
    if s[0] == '$':
        break
    s[-1] = s[-1][:-1]
    stack = []
    for c in s:
        if c == '':
            break
        if ')' not in c:
            stack.append(c)
        else:
            if c == ')':
                num = stack.pop()
            else:
                num = c[:-1]
            st = []
            while True:
                p = stack.pop()
                if '(' in p:
                    st.append(p[1:])
                    break
                st.append(p)
            stack.append(''.join(st[::-1]) * int(num))
    print(stack.pop())