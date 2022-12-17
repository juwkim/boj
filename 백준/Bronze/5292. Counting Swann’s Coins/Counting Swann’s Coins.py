for i in range(1, 1 + int(input())):
    a, b = i % 3, i % 5
    if a + b == 0:
        print('DeadMan')
    elif a == 0:
        print('Dead')
    elif b == 0:
        print('Man')
    else:
        print(i, end=' ')