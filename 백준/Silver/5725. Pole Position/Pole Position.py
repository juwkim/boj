g = lambda: [*map(int, input().split())]

while N:= int(input()):
    buf = [0] * N
    flag = True
    for i in range(N):
        C, P = g()
        
        idx = i + P
        if 0 <= idx < N and buf[idx] == 0:
            buf[idx] = C
        else:
            flag = False
    if flag:
        print(*buf)
    else:
        print(-1)