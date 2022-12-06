while 1:
    s = input()[::-1].split('=')
    a, b, c = map(int, [s[0]] + s[1].split('+'))
    print('True' if a == b + c else 'False')
    if not (a or b or c):
        break