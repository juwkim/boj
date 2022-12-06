while (s:=input()) != '0 0 0 0':
    h1, m1, h2, m2 = map(int, s.split())
    t = (h2 - h1) * 60 + m2 - m1
    if t < 0:
        t += 1440
    print(t)