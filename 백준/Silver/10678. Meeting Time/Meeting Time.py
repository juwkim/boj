import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
board1 = [[] for _ in range(N)]
board2 = [[] for _ in range(N)]
for _ in range(M):
    A, B, C, D = g()
    board1[A].append((B, C))
    board2[A].append((B, D))

def solve(res, board, cur, time):
    if cur == N:
        res.add(time)
        return
    for nxt, t in board[cur]:
        solve(res, board, nxt, time + t)

res1, res2 = set(), set()
solve(res1, board1, 1, 0)
solve(res2, board2, 1, 0)
res = res1 & res2
if res:
    print(min(res))
else:
    print("IMPOSSIBLE")