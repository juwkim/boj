N, M = map(int, input().split())
array = [0 for _ in range(N+1)]
def solve(M, check, buf):
    if M == 0:
        print(*buf)
        return
    for i in range(1, N+1):
        if check[i]:
            continue
        s = check.copy()
        s[i] = 1
        solve(M-1, s, buf + [i])
solve(M, array, []) 