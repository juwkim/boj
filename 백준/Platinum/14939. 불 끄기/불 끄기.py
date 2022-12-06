import copy
first_board = [[0] * 12] + [[0] + [int(i == "O") for i in input()] + [0] for _ in range(10)] + [[0] * 12]
min_cnt = 999

def solve(board, col, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return
    if col == 11:
        for r in range(2, 11):
            for c in range(1, 11):
                if board[r-1][c]:
                    cnt += 1
                    board[r][c-1] ^= 1
                    board[r][c] ^= 1
                    board[r][c+1] ^= 1
                    board[r+1][c] ^= 1
        if sum(board[10][1:11]) == 0:
            min_cnt = min(min_cnt, cnt)
        return
    solve(copy.deepcopy(board), col + 1, cnt)
    board[1][col] ^= 1
    board[1][col-1] ^= 1
    board[1][col+1] ^= 1
    board[2][col] ^= 1
    solve(board, col + 1, cnt + 1)

solve(first_board, 1, 0)
print(min_cnt if min_cnt != 999 else -1)