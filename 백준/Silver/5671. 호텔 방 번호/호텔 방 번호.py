g = lambda: [*map(int, input().split())]

while True:
    try:
        N, M = g()
        cnt = 0
        for i in range(N, M+1):
            tmp = str(i)
            cnt += len(tmp) == len(set(tmp))
        print(cnt)
    except:
        break