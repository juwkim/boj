while (k:=input().split()) != ['#']:
    for i in range(len(k)):
        if len(k[i]) > 1:
            k[i] = k[i][0]+k[i][1:-1][::-1]+k[i][-1]
    print(*k)