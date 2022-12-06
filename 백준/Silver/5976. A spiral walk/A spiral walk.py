def change():
    global state, i, j
    if state == 0:
        j += 1
    elif state == 1:
        i += 1
    elif state == 2:
        j -= 1
    else:
        i -= 1
        
g = lambda: [*map(int, input().split())]

N = int(input())
buf = [[0] * N for _ in range(N)]

i, j = 0, 0
state = 0
for num in range(1, 1 + N * N):
    buf[i][j] = num
    if state == 0:
        if j == N - 1 or buf[i][j+1]:
            state = 1
    elif state == 1:
        if i == N - 1 or buf[i+1][j]:
            state = 2
    elif state == 2:
        if j == 0 or buf[i][j-1]:
            state = 3
    else:
        if i == 0 or buf[i-1][j]:
            state = 0
    change()
for line in buf:
    print(*line)