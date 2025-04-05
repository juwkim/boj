import sys
input = lambda: sys.stdin.readline().rstrip()

I, N, K = map(int, input().split())
S = input()
stage = [[*input()] for _ in range(N)]
x, y = -1, -1
for i in range(N):
    for j in range(N):
        if stage[i][j] == '@':
            stage[i][j] = '.'
            x, y = i, j
            break
    if x != -1:
        break
dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
jump_cnt, ink = 0, 0
for cmd in input():
    match cmd:
        case 'U' | 'D' | 'L' | 'R':
            nx, ny = x + dx[cmd], y + dy[cmd]
            if 0 <= nx < N and 0 <= ny < N and stage[nx][ny] == '.':
                x, y = nx, ny
        case 'j':
            ink += 1
        case 'J':
            color = S[jump_cnt % I]
            jump_cnt += 1
            for i in range(N):
                for j in range(N):
                    if stage[i][j] != '.' and abs(x - i) + abs(y - j) <= ink:
                        stage[i][j] = color
            ink = 0
stage[x][y] = '@'
for l in stage:
    print(*l, sep='')