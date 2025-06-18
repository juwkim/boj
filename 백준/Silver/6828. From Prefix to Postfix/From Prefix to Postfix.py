import sys
input = lambda: sys.stdin.readline().rstrip()

while (line := input()) != '0':
    st = []
    for tok in reversed(line.split()):
        if tok in '+-':
            st.append(f"{st.pop()} {st.pop()} {tok}")
        else:
            st.append(tok)
    print(st[0])