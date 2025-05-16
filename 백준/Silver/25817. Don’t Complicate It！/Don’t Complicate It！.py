st = []
ans = 0
for c in input():
    if c == '(':
        st.append(1)
    elif c == ')':
        depth = st.pop()
        if st:
            st[-1] = max(st[-1], depth + 1)
        ans += depth
print(ans)