while True:
    l, w, h, v = map(int, input().split())
    if (l, w, h, v) == (0, 0, 0, 0):
        break
    if l == 0:
        l = v // w // h
    elif w == 0:
        w = v // h // l
    elif h == 0:
        h = v // l // w
    else:
        v = l * h * w
    print(l, w, h, v)