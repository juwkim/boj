import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(field, s, mask):
    def find():
        for i in range(s):
            for j in range(s):
                if field[i][j] == 'S':
                    return i, j
    i, j = find()
    dq = deque([(i, j)])
    visited = [bytearray(s) for _ in range(s)]
    visited[i][j] = True
    while dq:
        x, y = dq.popleft()
        if field[x][y] == 'X':
            return True
        for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if nx < 0 or nx >= s or ny < 0 or ny >= s or visited[nx][ny]:
                continue
            c = field[nx][ny]
            if c in 'GBR' and not mask & {'G': 1, 'B': 2, 'R': 4}[c]:
                continue
            visited[nx][ny] = True
            dq.append((nx, ny))
    return False

for _ in range(int(input())):
    s = int(input())
    field = [input() for _ in range(s)]
    for k in range(4):
        if any(bin(mask).count('1') == k and solve(field, s, mask) for mask in range(8)):
            print(k)
            break