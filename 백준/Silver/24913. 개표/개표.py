import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
cnt = [0] * (N + 2)
Max = 0
for _ in range(Q):
    cmd, x, num = g()
    if cmd == 1:
        cnt[num] += x
        if num != N + 1:
            Max = max(Max, cnt[num])
    else:
        p = 0
        ans = "NO"
        if Max < cnt[N + 1] + x:
            for i in range(1, N + 1):
                p += max(cnt[N + 1] + x - cnt[i] - 1, 0)
                if p >= num:
                    ans = "YES"
                    break
        print(ans)