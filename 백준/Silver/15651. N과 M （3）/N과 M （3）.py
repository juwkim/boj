N, M = map(int, input().split())
def solve(M, buf):
    global N
    if M == 0:
        print(*buf)
        return
    M -= 1
    for i in range(1, N+1):
        solve(M, buf + [i])
solve(M, [])