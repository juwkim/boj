import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

names, boards = [], []
for _ in range(int(input())):
    names.append(input())
    boards.append([g() for _ in range(5)])

m = int(input())
balls = g()
ans = []
for name, board in zip(names, boards):
    for ball in balls:
        for i in range(5):
            for j in range(5):
                if board[i][j] == ball:
                    board[i][j] = 0
                    break
            else:
                continue
            break
    tmp = [*zip(*board)]
    board.append([board[i][i] for i in range(5)])
    board.append([board[4 - i][i] for i in range(5)])
    board.extend(tmp)
    if any(all(num == 0 for num in l) for l in board):
        ans.append(name)
print(len(ans))
for name in ans:
    print(name)