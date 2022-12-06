for _ in range(int(input())):
    yp, lp, ys, ls = map(int, input().split())    
    a = yp * ys
    if yp > lp:
        b = (yp - lp) * ys + lp * ls
        c = (yp - lp) * ls + yp * ls
        print(min(a, b, c))
    else:
        print(min(a, lp * ls))