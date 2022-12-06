while True:
    s = input()[-1]
    if s == '!':
        break
    print('Quack!' if s == '?' else '*Nod*')