for i in range(1, 1 + int(input())):
    if i * i > 100:
        print('*' * 100 + '...')
    else:
        print('*' * (i * i))