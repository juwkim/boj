for i in range(1, 1 + int(input())):
    board = [input() for _ in range(int(input()))]
    if any('00' in row for row in board):
        print(f'Case {i}: Fallen')
    else:
        print(f'Case {i}: Standing')