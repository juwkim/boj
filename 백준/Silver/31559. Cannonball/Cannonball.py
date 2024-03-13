import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, S = g()
board = [g() for _ in range(N)]
S, P = S - 1, 1
ans = 0
check = set()
while 0 <= S < N and (S, P) not in check:
    q, v = board[S]
    check.add((S, P))
    if q:
        if v >= 0 and abs(P) >= v:
            ans += 1
            board[S][1] = -1
    elif P > 0:
        P = -P - v
    else:
        P = -P + v
    S += P
print(ans)