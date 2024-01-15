import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def check(s):
    return len(set(s)) == 1 and s[0] != "."

N = int(input())
board = [input() for _ in range(N)]

def solve():
    for i in range(N):
        for j in range(N - 2):
            if check(board[i][j:j+3]):
                return board[i][j]
    for i in range(N - 2):
        for j in range(N):
            if check([board[i+k][j] for k in range(3)]):
                return board[i][j]
    for i in range(N - 2):
        for j in range(N - 2):
            if check([board[i+k][j+k] for k in range(3)]):
                return board[i][j]
    for i in range(2, N):
        for j in range(N - 2):
            if check([board[i-k][j+k] for k in range(3)]):
                return board[i][j]
    return "ongoing"

print(solve())