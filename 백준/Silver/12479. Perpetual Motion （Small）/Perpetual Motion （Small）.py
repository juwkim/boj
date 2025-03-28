import sys
input = sys.stdin.readline
from itertools import product

dx = {'|': (1, -1), '-': (0, 0), '/': (1, -1), '\\': (1, -1)}
dy = {'|': (0, 0), '-': (1, -1), '/': (-1, 1), '\\': (1, -1)}

def solve(l):
    d = [l[i:i+C] for i in range(0, R*C, C)]
    visited = [bytearray(C) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if visited[i][j]:
                continue
            x, y = i, j
            while True:
                visited[x][y] = 1
                x, y = (x + dx[a[x][y]][d[x][y]]) % R, (y + dy[a[x][y]][d[x][y]]) % C
                if (x, y) == (i, j):
                    break
                if visited[x][y]:
                    return False
    return True

for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    a = [input() for _ in range(R)]
    ans = sum(solve(l) for l in product((0, 1), repeat=R*C)) % 1000003
    print(f"Case #{tc}: {ans}")