Map = [[''] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        Map[i][j] = ['|...', '|:::'][((i&1)+(j&1))&1]

_, white = input().split()
for item in white.split(','):
    if len(item) == 2:
        who = 'P'
        a, b = item
    else:
        who, a, b = item
    i, j = 8 - int(b), ord(a) - 97
    Map[i][j] = Map[i][j][:2] + who + Map[i][j][3]

_, black = input().split()
for item in black.split(','):
    if len(item) == 2:
        who = 'p'
        a, b = item
    else:
        who, a, b = item
    i, j = 8 - int(b), ord(a) - 97
    Map[i][j] = Map[i][j][:2] + who.lower() + Map[i][j][3]

print('+---+---+---+---+---+---+---+---+')
for i in range(8):
    print(*Map[i], '|', sep='')
    
    print('+---+---+---+---+---+---+---+---+')