while (s:= input()) != '99999':
    a = sum(map(int, s[:2]))
    if a % 2:
        direction = 'left'
    elif a:
        direction = 'right'
    print(direction, s[2:])