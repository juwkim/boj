for _ in range(int(input())):
    stack = 0
    flag = 'YES'
    for s in input():
        if s == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                flag = 'NO'
                break
    print('NO' if stack else flag)