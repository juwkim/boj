st = []
d = {'C': 12, 'H': 1, 'O': 16}
s, i = input(), 0
while i < len(s):
    match s[i]:
        case 'C'|'H'|'O': st.append(d[s[i]])
        case '(':         st.append('(')
        case ')':
            t = 0
            while st[-1] != '(':
                t += st.pop()
            st.pop()
            if i + 1 < len(s) and s[i + 1].isdigit():
                st.append(t * int(s[i + 1]))
                i += 1
            else:
                st.append(t)
        case _:
            st[-1] *= int(s[i])
    i += 1
print(sum(st))