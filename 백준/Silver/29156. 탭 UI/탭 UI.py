import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]
px = [0] * (N + 1)
for i in range(N): px[i + 1] = px[i] + l[i]
L = int(input())
ans = [0] * (N + 1)
for i in range(1, N + 1):
    # if px[i] - l[i - 1] / 2 - L / 2 <= 0:
    #     ans[i] = 0
    # else:
    ans[i] = max(0, min(px[N] - L, px[i] - l[i - 1] / 2 - L / 2))
for _ in range(int(input())):
    print("%.2f" % ans[int(input())])