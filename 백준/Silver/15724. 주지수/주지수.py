import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
cnt = [[0] * (M + 1)]
for i in range(N):
    line = [0] * (M + 1)
    Sum = 0
    for j, num in enumerate(g(), 1):
        Sum += num
        line[j] = Sum + cnt[i][j]
    cnt.append(line)
for _ in range(int(input())):
    x1, y1, x2, y2 = g()
    print(cnt[x2][y2] - cnt[x1 - 1][y2] - cnt[x2][y1 - 1] + cnt[x1 - 1][y1 - 1])