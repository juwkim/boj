import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
ans, buf = "YES", []
cnt = 0
for _ in range(M):
    A, B = g()
    if A + B > N:
        ans = "NO"
        break
    cur = ['X'] * N
    new_cnt = min(N, cnt + N - A - B)
    for i in range(N):
        if cnt <= i < new_cnt:
            continue
        if A:
            cur[i] = '+'
            A -= 1
        else:
            cur[i] = '-'
            B -= 1
    cnt = new_cnt
    buf.append(cur)
if cnt < N: ans = "NO"
print(ans)
if ans == "YES":
    for l in zip(*buf):
        print(*l, sep="")