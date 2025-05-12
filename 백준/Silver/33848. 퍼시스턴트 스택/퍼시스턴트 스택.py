import sys
input = sys.stdin.readline

st = []
logs = []
for _ in range(int(input())):
    cmd, *args = map(int, input().split())
    match cmd:
        case 1:
            st.append(args[0])
            logs.append((2,))
        case 2:
            logs.append((1, st.pop()))
        case 3:
            for _ in range(args[0]):
                cmd, *args = logs.pop()
                if cmd == 1:
                    st.append(args[0])
                else:
                    st.pop()
        case 4:
            print(len(st))
        case 5:
            print(st[-1] if st else -1)