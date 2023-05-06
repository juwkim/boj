while True:
    try:
        p = input()
        a, b = sorted(map(int, p.split()))
        s = ((86400 - a) * 43200 + 30 * (b - a)) // (b - a)
        h, s = divmod(s % 43200, 3600)
        if h == 0:
            h = 12
        m = s // 60
        ans = f'{p} {h:02d}:{m:02d}'
        print(ans)
    except:
        break