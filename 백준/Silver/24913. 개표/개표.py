import sys
g = lambda: map(int, sys.stdin.readline().split())

N, Q = g()
cnt = [0] * (N + 2)
for _ in range(Q):
    cmd, x, num = g()
    if cmd == 1:
        cnt[num] += x
    else:
        p = 0
        ans = "NO"
        for i in range(1, N + 1):
            p += max(cnt[N + 1] + x - cnt[i] - 1, 0)
            if p >= num:
                ans = "YES"
                break
        print(ans)