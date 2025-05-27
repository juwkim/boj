import sys
input = sys.stdin.readline

players = []
N = int(input())
for i in range(N):
    c, x = map(int, input().split())
    players.append((x, c, i))
players.sort()
res = [1e9] * N
lpos, r = -1e9, 0
for i in range(N):
    x, c, idx = players[i]
    if i and players[i - 1][1] != c:
        lpos = players[i - 1][0]
    while r < N and players[r][1] == c:
        r += 1
    if r == N:
        res[idx] = x - lpos
    else:
        res[idx] = min(x - lpos, players[r][0] - x)
for r in res:
    print(r)