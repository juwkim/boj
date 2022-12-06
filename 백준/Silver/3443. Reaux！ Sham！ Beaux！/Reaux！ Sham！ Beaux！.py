r = {'Kamen', 'Rock', 'Pierre', 'Stein', 'Ko', 'Koe', 'Sasso', 'Roccia',
     'Guu', 'Kamien', 'Piedra'}
s = {'Nuzky', 'Scissors', 'Ciseaux', 'Schere', 'Ollo', 'Olloo', 'Forbice',
     'Choki', 'Nozyce', 'Tijera'}
p = {'Papir', 'Paper', 'Feuille', 'Papier', 'Papir', 'Carta', 'Rete',
     'Paa', 'Papier', 'Papel'}

cnt = 1
while True:
    print(f'Game #{cnt}:')
    cnt += 1
    p1 = ''.join(input().split()[1:])
    p2 = ''.join(input().split()[1:])
    x, y = 0, 0
    while (msg:= input()) not in '-.':
        a, b = msg.split()
        if a in r:
            if b in s:
                x += 1
            elif b in p:
                y += 1
        elif a in s:
            if b in r:
                y += 1
            elif b in p:
                x += 1
        else:
            if b in r:
                x += 1
            elif b in s:
                y += 1
    
    if x == 1:
        print(f'{p1}: {x} point')
    else:
        print(f'{p1}: {x} points')
    if y == 1:
        print(f'{p2}: {y} point')
    else:
        print(f'{p2}: {y} points')
    if x == y:
        print('TIED GAME')
    elif x > y:
        print(f'WINNER: {p1}')
    else:
        print(f'WINNER: {p2}')

    if msg == '.':
        break
    print()