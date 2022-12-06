import sys
input = lambda: sys.stdin.readline().rstrip('\n')


def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1

g = lambda: [*map(int, input().split())]

N = int(input())
board = [[-1] * N for _ in range(N)]
cur = 0
flag = True
while flag:
    s = input()
    if s == 'QUIT':
        print('TIE GAME')
        break
    d, *num = s
    num = int(num[0])

    if d == 'L':
        try:
            idx = board[num-1].index(-1)
            board[num-1][:idx+1] = [cur] + board[num-1][:idx]
        except:
            board[num-1] = [cur] + board[num-1][:-1]

    elif d == 'R':
        try:
            idx = listRightIndex(board[num-1], -1)
            board[num-1][idx:] = board[num-1][idx+1:] + [cur]
        except:
            board[num-1] = board[num-1][1:] + [cur]
            
    elif d == 'T':
        idx = N - 1
        for i in range(N):
            if board[i][num-1] == -1:
                idx = i
                break
        
        for i in range(idx, 0, -1):
            board[i][num-1] = board[i-1][num-1]
        board[0][num-1] = cur
    else:
        idx = 0
        for i in range(N-1, -1, -1):
            if board[i][num-1] == -1:
                idx = i
                break
        
        for i in range(idx, N):
            board[i][num-1] = board[i-1][num-1]
        board[0][num-1] = cur
    
    score = [0, 0]
    for line in board:
        a = set(line)
        if a == {0}:
            score[0] += 1
        elif a == {1}:
            score[1] += 1
    for line in zip(*board):
        a = set(line)
        if a == {0}:
            score[0] += 1
        elif a == {1}:
            score[1] += 1
    if score[0] > score[1]:
        print('X WINS')
        flag = False
    elif score[0] < score[1]:
        print('O WINS')
        flag = False
    
    cur ^= 1