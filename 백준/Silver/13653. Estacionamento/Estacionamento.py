while True:
    try:
        C, N = map(int, input().split())
        space = [0] * C
        ans = 0
        pos = {}
        for _ in range(N):
            s = input().split()
            if s[0] == 'C':
                P, Q = map(int, s[1:])
                for i in range(C - Q + 1):
                    if all(num == 0 for num in space[i:i + Q]):
                        for j in range(i, i + Q):
                            space[j] = 1
                        pos[P] = (i, i + Q - 1)
                        ans += 10
                        break
            else:
                P = int(s[1])
                i, j = pos[P]
                for k in range(i, j + 1):
                    space[k] = 0
        print(ans)
    except:
        break