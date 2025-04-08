import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

def solve():
    N, M = g()
    cards = [g() for _ in range(N)]
    cnt = [0, 0]
    for i in range(N):
        for j in range(M):
            cnt[cards[i][j]] += 1
    if cnt[0] & 1 or cnt[1] & 1:
        return -1
    for i in range(N):
        if any(cards[i][j] == cards[i][j + 1] for j in range(M - 1)):
            return 1
        if i + 1 < N and any(cards[i][j] == cards[i + 1][j] for j in range(M)):
            return 1
    return -1
print(solve())