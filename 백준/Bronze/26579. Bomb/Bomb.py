for _ in range(int(input())):
    r, c = map(int, input().split())
    Map = [input() for _ in range(r)]
    ans, p, q = 0, 0, 0
    for i in range(r):
        for j in range(c):
            if Map[i][j] != '.':
                continue
            num = 0

            x = i - 1
            while x >= 0 and Map[x][j] != '#':
                num += Map[x][j] == '@'
                x -= 1

            x = i + 1
            while x < r and Map[x][j] != '#':
                num += Map[x][j] == '@'
                x += 1

            y = j - 1
            while y >= 0 and Map[i][y] != '#':
                num += Map[i][y] == '@'
                y -= 1

            y = j + 1
            while y < c and Map[i][y] != '#':
                num += Map[i][y] == '@'
                y += 1
            
            if num > ans:
                ans = num
                p, q = i, j
    print(f'{p}, {q}')