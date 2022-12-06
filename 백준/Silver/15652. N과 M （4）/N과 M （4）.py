N, M = map(int, input().split())
def solve(M, buf):
    if M == 0:
        print(*buf[1:])
        return
    M -= 1
    for i in range(1, N+1):
        if i >= buf[-1]:
            solve(M, buf + [i])
solve(M, [0])