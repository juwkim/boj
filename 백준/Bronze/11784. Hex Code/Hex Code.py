while True:
    try:
        msg = input()
        print(*[chr(int(msg[i:i+2], 16)) for i in range(0, len(msg), 2)], sep='')
    except:
        break