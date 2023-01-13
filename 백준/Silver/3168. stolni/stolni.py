def g(): return [*map(int, input().split())]

def get_ball_pos():

    idx = 0
    while mat[idx][0] != 'L':
        idx += 1
    
    pos = [idx]
    direction = -1
    for i in range(C - 1):
        if pos[-1] == 0:
            direction = 1
        elif pos[-1] == R - 1:
            direction = -1
        pos.append(pos[-1] + direction)

    return pos

R, C = map(int, input().split())
mat = [list(input()) for _ in range(R)]
pos = get_ball_pos()

for j in range(1, C):

    if mat[pos[j]][j] == '.':
        continue
    
    pipe = []
    for i in range(R):
        if mat[i][j] == '|':
            pipe.append(i)
            mat[i][j] = '.'

    pipe = [num - pipe[0] for num in pipe]
    while pos[j] in pipe:
        pipe = [num + 1 for num in pipe]
    
    for i in pipe:
        mat[i][j] = '|'

for j in range(1, C):
    mat[pos[j]][j] = 'L'

for line in mat:
    print(*line, sep='')