while True:
    try:
        l = input()
        n = len(l)
        check = set(l[i:] + l[:i] for i in range(n))
        t = int(l)
        ans = f"{l} is cyclic"
        for i in range(1, n + 1):
            p = str(t * i)[-n:].zfill(n)
            if p not in check:
                ans = f"{l} is not cyclic"
                break
        print(ans)
    except:
        break