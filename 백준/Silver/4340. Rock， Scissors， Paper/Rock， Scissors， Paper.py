for _ in range(int(input())):
    r, c, n = map(int, input().split())
    Map = [[''] * (c + 2)] + [[''] + list(input()) + [''] for _ in range(r)] + [[''] * (c + 2)]
    
    for _ in range(n):
        new = [[''] * (c + 2) for _ in range(r + 2)]
        
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                tmp = [Map[i][j + 1], Map[i][j - 1], Map[i + 1][j], Map[i - 1][j]]
                if Map[i][j] == 'R' and 'P' in tmp:
                    new[i][j] = 'P'
                elif Map[i][j] == 'S' and 'R' in tmp:
                    new[i][j] = 'R'
                elif Map[i][j] == 'P' and 'S' in tmp:
                    new[i][j] = 'S'
                else:
                    new[i][j] = Map[i][j]
        Map = new
    for line in Map[1:-1]:
        print(*line[1:-1], sep='')
    print()