import sys
input = sys.stdin.readline

N = int(input())
x, y, r = zip(*[[*map(int, input().split())] for _ in range(N)])
pos = -1
for i in range(N):
    if x[i] == 0 and y[i] == 0:
        pos = i
        break
visited = bytearray(N)
visited[pos] = 1
for _ in range(N - 2):
    for i in range(N):
        if visited[i]:
            continue
        x1, y1, r1 = x[i], y[i], r[i]
        x2, y2, r2 = x[pos], y[pos], r[pos]
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 + r2) ** 2:
            visited[i] = 1
            pos = i
            break
idx = visited.find(0)
print(x[idx], y[idx])