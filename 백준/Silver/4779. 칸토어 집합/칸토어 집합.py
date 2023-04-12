def solve(l, r, n):
    if n == 0:
        return
    d = (r + 1 - l) // 3
    for i in range(l + d, l + 2 * d):
        buf[i] = ' '
    solve(l, l + d - 1, n - 1)
    solve(l + 2 * d, r, n - 1)

ans = [None for _ in range(13)]
while True:
    try:
        N = int(input())
        if ans[N] is None:
            buf = ['-' for _ in range(3 ** N)]
            solve(0, 3 ** N - 1, N)
            ans[N] = "".join(buf)
        print(ans[N])
    except:
        break