import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N, M, K = g()
board = [list(input()) for _ in range(N)]
cnt = [[Counter() for _ in range(K)] for _ in range(K)]
for i in range(N):
    for j in range(M):
        cnt[i % K][j % K][board[i][j]] += 1
Max = [[cnt[i][j].most_common(1)[0][0] for j in range(K)] for i in range(K)]
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != Max[i % K][j % K]:
            ans += 1
            board[i][j] = Max[i % K][j % K]
print(ans)
for l in board:
    print("".join(l))