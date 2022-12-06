while 1:
    try:
        a, b, c, d = 0, 0, 0, 0
        for s in input():
            if 'a' <= s <= 'z': a += 1
            elif 'A' <= s <= 'Z': b += 1
            elif '0' <= s <= '9': c += 1
            else: d += 1
        print(a, b, c, d)
    except:
        break