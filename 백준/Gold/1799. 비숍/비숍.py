import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
board = [g() for _ in range(N)]
ans = [0, 0]
diagonal = [False] * (2 * N - 1)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            diagonal[i - j + N - 1] = True

def solve(line, cnt, idx):
    global ans
    if line > 2 * N - 1:
        ans[idx] = max(ans[idx], cnt)
        return
    flag = True
    for i in range(N):
        j = line - i
        if j < 0 or j >= N or board[i][j] == 0 or diagonal[i - j + N - 1] == False:
            continue
        flag = False
        diagonal[i - j + N - 1] = False
        solve(line + 2, cnt + 1, idx)
        diagonal[i - j + N - 1] = True
    if flag:
        solve(line + 2, cnt, idx)
solve(0, 0, 0)
solve(1, 0, 1)
print(sum(ans))