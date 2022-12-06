g = lambda: [*map(int, input().split())]

N, X = g()
buf = [g() for _ in range(N)]
for i in range(N-1):
    if buf[i][0] > buf[i+1][0] and buf[i][1] == 1 and buf[i+1][1] == 0:
        buf[i][0], buf[i+1][0] = buf[i+1][0], buf[i][0]
    elif buf[i][0] < buf[i+1][0] and buf[i][1] == 0 and buf[i+1][1] == 1:
        buf[i][0], buf[i+1][0] = buf[i+1][0], buf[i][0]
cnt = 0
for i in range(N):
    a, b = buf[i]
    if a > X and b == 0:
        cnt += 1
    elif a <= X and b == 1:
        cnt += 1
print(cnt)