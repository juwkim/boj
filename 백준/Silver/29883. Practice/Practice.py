import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, M = map(int, input().split())
px = [0] * (N + 1)
for i, num in enumerate(g()):
    px[i + 1] = px[i] + num
ans = [0] * 1000001
for i in range(N):
    for j in range(i + 1, N + 1):
        idx = px[j] - px[i]
        if idx < 1000000:
            ans[idx] = 1
for num in g():
    if ans[num]:
        print("JAH")
    else:
        print("EI")