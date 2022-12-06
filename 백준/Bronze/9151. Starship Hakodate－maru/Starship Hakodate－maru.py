while(True):
    n = int(input())
    if n == 0:
        break
    max_num, y = 0, 0
    t = y*(y+1)*(y+2)//6
    while n - t >= 0:
        x = 0
        while x**3 <= n - t:
            if x**3 + t > max_num:
                max_num = x**3 + t
            x += 1
        if max_num == n:
            break
        y += 1
        t = y*(y+1)*(y+2)//6
    print(max_num)