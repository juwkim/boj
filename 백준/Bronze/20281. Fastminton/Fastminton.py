score = [0, 0]
set_score = [0, 0]

server = 0
for c in input():
    if c == 'R':
        server ^= 1
    if c == 'Q':
        a, b = score
        x, y = set_score
        if score[server] == 2:
            if server == 0:
                print(f'{a} (winner) - {b}')
            else:
                print(f'{a} - {b} (winner)')            
        elif server == 0:
            print(f'{a} ({x}*) - {b} ({y})')
        else:
            print(f'{a} ({x}) - {b} ({y}*)')
    else:
        set_score[server] += 1
        if (set_score[server] - set_score[1 - server] >= 2 and set_score[server] >= 5) or set_score[server] >= 10:
            set_score = [0, 0]
            score[server] += 1