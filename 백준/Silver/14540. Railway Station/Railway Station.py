import sys
input = lambda: sys.stdin.readline().rstrip()
while N:=int(input()):
    while (s:=input()) != '0':
        st, i = [], 0
        ans = "Yes"
        for num in map(int, s.split()):
            if not st or st[-1] != num:
                while i < N and i != num:
                    i += 1
                    st.append(i)
            if st[-1] == num:
                st.pop()
            elif i == N:
                ans = "No"
                break
        print(ans)
    print()