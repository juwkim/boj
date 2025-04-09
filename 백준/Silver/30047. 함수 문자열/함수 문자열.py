def solve():
    st = []
    for c in input():
        if c in "gf":
            st.append(c)
        else:
            num = 0
            while st and st[-1] != 'f':
                cur = st.pop()
                if cur == 'g':
                    num += 1
                elif not st or st[-1] != 'f':
                    return -1
                else:
                    num = min(num, cur)
                    st.pop()
            st.append(num)
    return st.pop() if len(st) == 1 and type(st[-1]) == int else -1

print(solve())