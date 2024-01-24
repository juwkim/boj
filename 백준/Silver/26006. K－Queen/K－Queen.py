import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
R, C = g()
state = [[0] * 3 for _ in range(3)]
if R == 1:
    state[0][0] = 1
    state[0][1] = 1
    state[0][2] = 1
elif R == N:
    state[2][0] = 1
    state[2][1] = 1
    state[2][2] = 1
if C == 1:
    state[0][0] = 1
    state[1][0] = 1
    state[2][0] = 1
elif C == N:
    state[0][2] = 1
    state[1][2] = 1
    state[2][2] = 1
for _ in range(K):
    r, c = g()
    r -= R - 1
    c -= C - 1
    if 0 <= r <= 2:
        for i in range(3):
            state[r][i] = 1
    if 0 <= c <= 2:
        for i in range(3):
            state[i][c] = 1
    if 0 <= r + c <= 4:
        for i in range(3):
            if 0 <= r + c - i <= 2:
                state[i][r + c - i] = 1
    if -2 <= r - c <= 2:
        for i in range(3):
            if 0 <= r - c + i <= 2:
                state[r - c + i][i] = 1
p = sum(state[i][j] for i in range(3) for j in range(3))
if p == 9:
    print("CHECKMATE")
elif state[1][1] == 1:
    print("CHECK")
elif p == 8:
    print("STALEMATE")
else:
    print("NONE")