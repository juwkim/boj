while True:
    l = input()
    if l == "()":
        break
    st = []
    i = 0
    while i < len(l):
        c = l[i]
        if c == ' ' or c == '(':
            i += 1
        elif c == ')':
            y, x, p = st.pop(), st.pop(), st.pop()
            st.append(p * (x + y) + (1 - p) * (x - y))
            i += 1
        else:
            tmp = ""
            while i < len(l) and l[i] != ' ' and l[i] != ')':
                tmp += l[i]
                i += 1
            st.append(float(tmp))
    ans = st.pop()
    print(f"{ans:.2f}")