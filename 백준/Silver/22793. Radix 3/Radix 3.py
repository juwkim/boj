for s in map(str.rstrip, open(0)):
    ans = []
    n = int(s)
    while True:
        n, r = divmod(n, 3)
        match r:
            case 0:
                ans.append('0')
            case 1:
                ans.append('1')
            case 2:
                ans.append('-')
                n += 1
        if n == 0:
            break
    print(f"{s} = {''.join(ans)[::-1]} GSC")