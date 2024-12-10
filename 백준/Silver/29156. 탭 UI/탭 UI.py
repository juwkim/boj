import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]
px = [0] * (N + 1)
for i in range(N): px[i + 1] = px[i] + l[i]
L = int(input())
ans = [0] * (N + 1)
for i in range(1, N + 1):
    if px[i] - l[i - 1] / 2 <= L / 2:
        ans[i] = 0
    elif px[N] - (px[i] - l[i - 1] / 2) <= L / 2:
        ans[i] = px[N] - min(px[N], L)
    else:
        ans[i] = px[i] - l[i - 1] / 2 - L / 2
for _ in range(int(input())):
    print("%.2f" % ans[int(input())])