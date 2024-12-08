import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
vote = [0] * (N + 1)
Max, cnt = 0, -N
for _ in range(Q):
    cmd, x, num = g()
    if cmd == 1:
        vote[num - 1] += x
        if num == N + 1:
            cnt += x * N
        else:
            Max = max(Max, vote[num - 1])
            cnt -= x
    else:
        if Max < vote[N] + x and num <= cnt + x * N:
            ans = "YES"
        else:
            ans = "NO"
        print(ans)