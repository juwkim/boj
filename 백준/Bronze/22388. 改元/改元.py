while (s:= input()) != '#':
    g, y, m, d = s.split()
    y, m, d = map(int, [y, m, d])
    if y * 365 + m * 30 + d > 11465:
        y -= 30
        g = '?'
    print(g, y, m, d)