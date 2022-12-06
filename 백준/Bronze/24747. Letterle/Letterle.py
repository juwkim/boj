s = input()
for j in range(7):
    p = input()
    if s == p:
        print('WINNER')
        break
    if j == 6:
        print('LOSER')
        break
    for i in range(5):
        if p[i] == s[i]:
            print('G', end='')
        elif p[i] in s:
            print('Y', end='')
        else:
            print('X', end='')
    print()