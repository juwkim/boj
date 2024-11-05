import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
board = [[input().count('P'), False] for _ in range(n)]
board[r - 1][1] = True
cur = n - 1
while cur and board[cur][0] == 0: cur -= 1
for _ in range(sum(l for l, _ in board)):
    s = input()
    board[cur][0] -= 1
    if s[-4] == 'y':
        cnt = s.count('y') - 3
        l = board[cur]
        del board[cur]
        board.insert(cur - cnt, l)
    while cur and board[cur][0] == 0:
        cur -= 1
for i in range(n):
    if board[i][1]:
        r = i + 1
        break
print(r)