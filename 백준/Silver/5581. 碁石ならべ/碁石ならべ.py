import sys
input = sys.stdin.readline

st = []
for i in range(int(input())):
    color = int(input())
    if st and st[-1][0] == color:
        st[-1][1] += 1
    elif i & 1:
        _, cnt = st.pop()
        if st:
            st[-1][1] += cnt + 1
        else:
            st.append([color, cnt + 1])
    else:
        st.append([color, 1])
print(sum(cnt for c, cnt in st if c == 0))