R, C = int(input()), int(input())
Map = [[*input()] for _ in range(R)]

x, y = 0, 0
while True:
    if Map[x][y] == 1:
        ans = 'cykel'
        break
    elif Map[x][y] == 'A':
        ans = 'sushi'
        break
    elif Map[x][y] == 'B':
        ans = 'samuraj'
        break
    elif Map[x][y] == '<':
        Map[x][y] = 1
        y -= 1
    elif Map[x][y] == '>':
        Map[x][y] = 1
        y += 1
    elif Map[x][y] == 'v':
        Map[x][y] = 1
        x += 1
    else:
        Map[x][y] = 1
        x -= 1
print(ans)