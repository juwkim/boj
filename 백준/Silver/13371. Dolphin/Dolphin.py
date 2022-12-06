for _ in range(int(input())):
    n = int(input())
    
    num = 3
    while n > 0:
        n -= num
        num += 3
    
    num -= 3
    n += num
    num //= 3
    
    n -= num
    if n <= 0:
        print(num, 'dolphin' + 's' * (num > 1))
    else:
        n -= num
        if n <= 0:
            print(num, 'jump' + 's' * (num > 1))
        else:
            print('splash')