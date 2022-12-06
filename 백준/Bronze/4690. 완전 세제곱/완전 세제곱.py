for a in range(3, 101):
    for b in range(2, 100):
        c = b
        d = a**3 - b**3 - c**3
        while d >= c**3:
            d = round(d**(1/3), 5)
            if d == int(d):
                print(f'Cube = {a}, Triple = ({b},{c},{int(d)})')
            c += 1
            d = a**3 - b**3 - c**3