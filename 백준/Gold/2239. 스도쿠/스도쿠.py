import sys
def find_val(r, c):
    nums = {*range(1, 10)}
    row = {*board[r]}
    col = {board[i][c] for i in range(9)}
    r, c = r // 3 * 3, c // 3 * 3
    square = set()
    for i in range(r, r+3):
        square.update([board[i][j] for j in range(c, c+3)])
    return sorted(nums - row - col - square)

def solve(x):
    if x == 81:
        return 1
    r, c = divmod(x, 9)
    if board[r][c]:
        if solve(x+1):
            return 1
    else:
        nums = find_val(r, c)
        for num in nums:
            board[r][c] = num
            if solve(x+1):
                return 1
            board[r][c] = 0

board = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(9)]
solve(0)
for row in board:
    print(*row, sep="")