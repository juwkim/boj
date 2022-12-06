i = 1
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if a == -1 and c > b:
        t = (c**2 - b**2)**.5
        state = f'a = {t:#.3f}'
    elif b == -1 and c > a:
        t = (c**2 - a**2)**.5
        state = f'b = {t:#.3f}'
    elif c == -1:
        t = (a**2 + b**2)**.5
        state = f'c = {t:#.3f}'
    else:
        state = 'Impossible.'
    print(f'Triangle #{i}\n{state}\n')
    i += 1