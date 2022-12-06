while True:
    try:
        n = int(input())
        i = 1
        
        num = n
        while num > 0:
            num -= i
            i += 1
        num += i - 1
        
        a = num
        b = i - num
        if i&1:
            print(f'TERM {n} IS {a}/{b}')
        else:
            print(f'TERM {n} IS {b}/{a}')
        
    except:
        break