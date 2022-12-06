g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    size = int(input())
    board = [g() for _ in range(size)]
    a = sum(board[i][i] for i in range(size))
    b = sum(board[i][size-1-i] for i in range(size))
    if a != b:
        print('Not a magic square')
    elif any(sum(row) != a for row in board):
        print('Not a magic square')
    elif any(sum(col) != a for col in zip(*board)):
        print('Not a magic square')
    else:
        print('Magic square of size', size)