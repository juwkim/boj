import sys
input = lambda: sys.stdin.readline().rstrip()
while N:=int(input()):
    while True:
        s = input()
        if s == '0':
            break
        st = []
        i = 1
        ans = "Yes"
        for num in map(int, s.split()):
            if not st or st[-1] != num:
                while i <= N:
                    st.append(i)
                    i += 1
                    if i - 1 == num:
                        break
            if st[-1] == num:
                st.pop()
            elif i == N + 1:
                ans = "No"
                break
        print(ans)
    print()    