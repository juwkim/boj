while (n:=int(input())):
    count = 1
    res = [n]
    while True:
        n = int(str(n**2).zfill(8)[2:6])
        if n in res:
            break
        else:
            res.append(n)
            count += 1
    print(count)