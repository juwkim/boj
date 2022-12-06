def is_sum_one(i, j, k):

    Sum = 0
    
    if i - k >= 0:
        Sum += sum(board[i-k][max(0, j-k):min(j+k+1, M)])
        if Sum > 1:
            return False
    
    if i + k < N:
        Sum += sum(board[i+k][max(0, j-k):min(j+k+1, M)])
        if Sum > 1:
            return False
    
    if j - k >= 0:
        Sum += sum(board[p][j-k] for p in range(max(0, i-k+1), min(i+k, N)))
        if Sum > 1:
            return False
    
    if j + k < M:
        Sum += sum(board[p][j+k] for p in range(max(0, i-k+1), min(i+k, N)))
        if Sum > 1:
            return False

    return Sum == 1


def check(i, j):
    
    for k in range(1, 10):
        if not is_sum_one(i, j, k):
            return False
    return True


def solve():
    for i in range(N):
        for j in range(M):
            if board[i][j] and check(i, j):
                print(i, j)
                return
    print(-1)
    return

N, M = map(int, input().split())
board = [[*map(int, input())] for _ in range(N)]
solve()