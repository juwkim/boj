import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def check(s):
    cnt = (s[0] in "IE" and s[1] in "NS" and s[2] in "FT" and s[3] in "PJ")
    cnt += (s[3] in "IE" and s[2] in "NS" and s[1] in "FT" and s[0] in "PJ")
    return cnt

N, M = g()
board = [input() for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M - 3):
        ans += check(board[i][j:j + 4])
for i in range(N - 3):
    for j in range(M):
        ans += check([board[i + k][j] for k in range(4)])
for i in range(N - 3):
    for j in range(M - 3):
        ans += check([board[i + k][j + k] for k in range(4)])
for i in range(3, N):
    for j in range(M - 3):
        ans += check([board[i - k][j + k] for k in range(4)])
print(ans)