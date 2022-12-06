speed, time, dist = 0, 0, 0
while True:
    try:
        l = input().split()
        h, m, s = map(int, l[0].split(':'))
        cur = h * 3600 + m * 60 + s
        dist += (cur - time) * speed
        time = cur
        if len(l) == 2:
            speed = int(l[1])
        else:
            print(f'{l[0]} {dist / 3600:.2f} km')               
    except:
        break