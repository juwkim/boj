tc = 1
while True:
    r, c = map(int, input().split())
    if r == 0: break
    crossword = [input() for _ in range(r)]
    i = 1
    across, down = [f'Crossword puzzle {tc}', "Across"], ["Down"]
    for x in range(r):
        for y in range(c):
            plus = False
            if (y == 0 or crossword[x][y-1] == '@') and crossword[x][y] != '@':
                l = 1
                while y + l < c and crossword[x][y+l] != '@': l += 1
                if l >= 3:
                    if i < 10: across.append(f"{i}.  ({l})")
                    else:      across.append(f"{i}. ({l})")
                    plus = True
            if (x == 0 or crossword[x-1][y] == '@') and crossword[x][y] != '@':
                l = 1
                while x + l < r and crossword[x+l][y] != '@': l += 1
                if l >= 3:
                    if i < 10: down.append(f"{i}.  ({l})")
                    else:      down.append(f"{i}. ({l})")
                    plus = True
            i += plus
    print(*across, *down, sep='\n', end='\n\n')
    tc += 1