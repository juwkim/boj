N, M = map(int, input().split())
def solve(M, buf):
    if M == 0:
        print(*buf[1:])
        return
    M -= 1
    for i in range(max(1, buf[-1]), N + 1):
        solve(M, buf + [i])
solve(M, [0])