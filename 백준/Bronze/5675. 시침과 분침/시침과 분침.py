while True:
    try:
        print('NY'[int(input()) % 6 == 0])
    except:
        break