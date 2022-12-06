g = lambda: [*map(int, input().split())]

Map = [g() for _ in range(19)]
def solve():
    for i in range(19):
        num = sum(Map[i][:4])
        for j in range(4, 19):
            num += Map[i][j]
            if all(val == 1 for val in Map[i][j-4:j+1]) and (j == 18 or Map[i][j+1] != 1) and (j == 4 or Map[i][j-5] != 1):
                return (1, i + 1, j - 3)
            if all(val == 2 for val in Map[i][j-4:j+1]) and (j == 18 or Map[i][j+1] != 2) and (j == 4 or Map[i][j-5] != 2):
                return (2, i + 1, j - 3)
            num -= Map[i][j-4]
    
    for j in range(19):
        num = sum(Map[i][j] for i in range(4))
        for i in range(4, 19):
            num += Map[i][j]
            if all(Map[k][j] == 1 for k in range(i-4, i+1)) and (i == 18 or Map[i+1][j] != 1) and (i == 4 or Map[i-5][j] != 1):
                return (1, i - 3, j + 1)
            if all(Map[k][j] == 2 for k in range(i-4, i+1)) and (i == 18 or Map[i+1][j] != 2) and (i == 4 or Map[i-5][j] != 2):
                return (2, i - 3, j + 1)
            num -= Map[i-4][j]
    for i in range(15):
        num = sum(Map[i + j][j] for j in range(4))
        for j in range(4, 19 - i):
            num += Map[i + j][j]
            if all(Map[i + k][k] == 1 for k in range(j-4, j+1)) and (j == 18 - i or Map[i + j + 1][j + 1] != 1) and (j == 4 or Map[i + j - 5][j - 5] != 1):
                return (1, i + j - 3, j - 3)
            if all(Map[i + k][k] == 2 for k in range(j-4, j+1)) and (j == 18 - i or Map[i + j + 1][j + 1] != 2) and (j == 4 or Map[i + j - 5][j - 5] != 2):            
                return (2, i + j - 3, j - 3)
            num -= Map[i + j - 4][j - 4]    
    for j in range(1, 15):
        num = sum(Map[i][i + j] for i in range(4))
        for i in range(4, 19 - j):
            num += Map[i][i + j]
            if all(Map[k][k + j] == 1 for k in range(i-4, i+1)) and (i == 18 - j or Map[i + 1][i + j + 1] != 1) and (i == 4 or Map[i - 5][i + j - 5] != 1):
                return (1, i - 3, i + j - 3)
            if all(Map[k][k + j] == 2 for k in range(i-4, i+1)) and (i == 18 - j or Map[i + 1][i + j + 1] != 2) and (i == 4 or Map[i - 5][i + j - 5] != 2):            
                return (2, i - 3, i + j - 3)
            num -= Map[i - 4][i + j - 4]
    
    for j in range(4, 19):
        num = sum(Map[i][j - i] for i in range(4))
        for i in range(4, 1 + j):
            num += Map[i][j - i]
            if all(Map[k][j - k] == 1 for k in range(i-4, i+1)) and (i == j or Map[i + 1][j - i - 1] != 1) and (i == 4 or Map[i - 5][j - i + 5] != 1):
                return (1, i + 1, j - i + 1)
            if all(Map[k][j - k] == 2 for k in range(i-4, i+1)) and (i == j or Map[i + 1][j - i - 1] != 2) and (i == 4 or Map[i - 5][j - i + 5] != 2):            
                return (2, i + 1, j - i + 1)
            num -= Map[i - 4][j - i + 4]
    
    for j in range(1, 15):
        num = sum(Map[18 - i][i + j] for i in range(4))
        for i in range(4, 19 - j):
            num += Map[18 - i][i + j]
            if all(Map[18 - k][k + j] == 1 for k in range(i-4, i+1)) and (i == 18 - j or Map[17 - i][i + j + 1] != 1) and (i == 4 or Map[23 - i][i + j - 5] != 1):
                return (1, 21 - i, i + j - 3)
            if all(Map[18 - k][k + j] == 2 for k in range(i-4, i+1)) and (i == 18 - j or Map[17 - i][i + j + 1] != 2) and (i == 4 or Map[23 - i][i + j - 5] != 2):            
                return (2, 21 - i, i + j - 3)
            num -= Map[22 - i][i + j - 4]            
    return 0, 0, 0

a, r, c = solve()
if a:
    print(a)
    print(r, c)
else:
    print(0)