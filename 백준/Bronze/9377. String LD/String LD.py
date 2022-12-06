while n := int(input()):
    cnt = 0
    s = [input() for _ in range(n)]
    while True:
        s = [i[1:] for i in s]
        p = len(s) - len(set(s))
        if '' in s or p:
            print(cnt)
            break
        cnt += 1