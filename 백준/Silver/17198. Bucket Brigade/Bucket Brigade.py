from collections import deque
Map = []
x, y = -1, -1
for i in range(10):
    line = input()
    Map.append(list(line))
    if y == -1:
        x, y = i, line.find('B')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dq = deque([(0, x, y)])
def bfs():
    while dq:
        cnt, p, q = dq.popleft()
        for i, j in [(p + a, q + b) for a, b in zip(dx, dy)]:
            if 0 <= i < 10 and 0 <= j < 10:
                if Map[i][j] == 'L':
                    return cnt
                if Map[i][j] == '.':
                    Map[i][j] = ''
                    dq.append((cnt + 1, i, j))
print(bfs())