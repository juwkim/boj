for s in open(0):
    n = int(s.split('/')[1])
    ans, x = 0, n + 1
    while True:
        y, r = divmod(n * x, x - n)
        if y < x:
            break
        ans += r == 0
        x += 1
    print(ans)