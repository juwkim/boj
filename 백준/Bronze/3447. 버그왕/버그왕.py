while True:
    try:
        s = input()
        while 'BUG' in s:
            s = s.replace('BUG', '')
        print(s)
    except:
        break