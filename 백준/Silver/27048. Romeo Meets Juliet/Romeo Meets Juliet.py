g = lambda: [*map(int, input().split())]
N, P, C = g()
board = [0] * (P + 1)
for _ in range(N):
    board[int(input())] += 1
ans = 0
l, r, cnt = 1, 1, 0
while r <= P:
    if cnt <= C:
        ans = max(ans, r - l)
    if cnt < C or (cnt == C and board[r] == 0):
        cnt += board[r]
        r += 1
    elif cnt >= C:
        cnt -= board[l]
        l += 1
print(ans)