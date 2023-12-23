import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

buf = []
N = int(input())
for _ in range(N):
    t, d = input().split()
    idx = t.index(':')
    H = int(t[:idx])
    if H == 12:
        H = 0
    M = int(t[idx + 1:idx + 3])
    timezone = t[idx + 3:]
    if timezone == 'pm':
        H += 12
    time = H * 60 + M
    buf.append([time, int(d)])

buf.sort()
for i in range(1, N):
    buf[i][1] += buf[i - 1][1]

Min = min(buf[i][1] for i in range(N))
ans = 0
for i in range(N - 1):
    if buf[i][1] == Min:
        ans += buf[i + 1][0] - buf[i][0]
if buf[N - 1][1] == Min:
    ans += 24 * 60 - buf[N - 1][0]
print(ans)