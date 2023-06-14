n, d = input().split()
n, d = int(n), float(d)

while True:
    try:
        t, *l = input().split()
        second = 0
        for time in l:
            h, m, s = map(int, time.split(':'))
            second += h * 3600 + m * 60 + s
        
        sec_per_km = round(second / d)
        m, s = divmod(sec_per_km, 60)
        print(f"{t:>3}: {m}:{s:02} min/km")
    except EOFError:
        break
    except Exception:
        print(f"{t:>3}: -")