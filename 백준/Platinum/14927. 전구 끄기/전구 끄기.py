import copy
import sys
input = sys.stdin.readline
N = int(input())
first_board = [[0] * (N + 2)] + [[0] + [*map(int, input().rstrip().split())] + [0] for _ in range(N)] + [[0] * (N + 2)]
min_cnt = 999

def solve(board, col, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return
    if col == N + 1:
        for r in range(2, N+1):
            for c in range(1, N+1):
                if board[r-1][c]:
                    cnt += 1
                    board[r][c-1] ^= 1
                    board[r][c] ^= 1
                    board[r][c+1] ^= 1
                    board[r+1][c] ^= 1
        if sum(board[N][1:N+1]) == 0:
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