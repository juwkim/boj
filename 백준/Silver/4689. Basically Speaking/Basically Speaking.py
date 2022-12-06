while True:
    try:        
        num, *l = input().split()
        base_from, base_to = map(int, l)
        num = int(num, base_from)
        
        ans = ''
        while True:
            num, q = divmod(num, base_to)
            ans = hex(q)[2:] + ans
            if num == 0:
                break
        
        if len(ans) < 8:
            print(ans.rjust(7).upper())
        else:
            print('  ERROR')
    except:
        break