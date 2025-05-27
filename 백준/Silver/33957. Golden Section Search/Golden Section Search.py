import sys
input = sys.stdin.readline

N = int(input())
pxl, pxr = [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    L, R = map(int, input().split())
    pxl[i + 1] = pxl[i] + L
    pxr[i + 1] = pxr[i] + R
ans = 0
for i in range(1, N):
    lo1, hi1 = pxl[i], pxr[i]
    lo2, hi2 = pxl[N] - pxl[i], pxr[N] - pxr[i]
    if lo1 <= hi2 and lo2 <= hi1:
        ans += 1
print(ans)