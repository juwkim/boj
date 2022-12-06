while True:
    t = [0, 0]
    while True:
        line = input()
        if line in '$$$###':
            break
        idx = line[0] == '+'
        h, m = line[1:].replace(".", ":").split(":")
        if h:
            t[idx] += int(h) * 60
        if m:
            t[idx] += int(m)
    h, m = divmod(t[1] - t[0], 60)
    print("%d:%02d" % (h, m))
    if line == '###':
        break