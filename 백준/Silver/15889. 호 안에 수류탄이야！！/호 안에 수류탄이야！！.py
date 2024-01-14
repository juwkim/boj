import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = "권병장님, 중대장님이 찾으십니다"
N = int(input())
if N > 1:
    pos = g()
    dpos = g()
    cur = 0
    for i in range(N - 1):
        if pos[i] > cur:
            ans = "엄마 나 전역 늦어질 것 같아"
            break
        cur = max(cur, pos[i] + dpos[i])
    if pos[-1] > cur:
        ans = "엄마 나 전역 늦어질 것 같아"
print(ans)