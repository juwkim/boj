while (N:= input()) != '0':
    cnt, cur = 1, N[0]
    for c in N[1:]:
        if cur == c:
            cnt += 1
        else:
            print(cnt, cur, sep="", end="")
            cur = c
            cnt = 1
    print(cnt, cur, sep="")