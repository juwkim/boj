for i in range(1, 1 + int(input())):
    a, b = i % 7, i % 11
    if a == 0 and b == 0:
        ans = 'Wiwat!'
    elif a == 0:
        ans = 'Hurra!'
    elif b == 0:
        ans = 'Super!'
    else:
        ans = i
    print(ans)