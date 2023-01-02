def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):
    R, C = g()
    mat = [[*input()] for _ in range(R)]
    flag = True
    for i in range(R):
        for j in range(C):
            if mat[i][j] != '#':
                continue
            if i + 1 == R or j + 1 == C:
                break
            if (mat[i][j+1], mat[i+1][j], mat[i+1][j+1]) != ('#', '#', '#'):
                break

            mat[i][j] = '/'
            mat[i][j+1] = '\\'
            mat[i+1][j] = '\\'
            mat[i+1][j+1] = '/'
            
        else:
            continue
        flag = False
        break

    print(f'Case #{t}:')
    if flag:
        for line in mat:
            print(*line, sep='')
    else:
        print('Impossible')