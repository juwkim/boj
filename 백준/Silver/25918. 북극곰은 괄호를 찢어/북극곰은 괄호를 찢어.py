input()
ans, st = 0, []
for c in input():
    if st and st[-1] != c:
        st.pop()
    else:
        st.append(c)
        ans = max(ans, len(st))
if st:
    ans = -1
print(ans)