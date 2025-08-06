import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [input() for _ in range(N)]
crossed = [bytearray(N) for _ in range(N)]
for _ in range(int(input())):
    L = len(w:=input())
    for i in range(N):
        for j in range(N):
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                if all(0 <= i + dx * k < N and 0 <= j + dy * k < N and grid[i + dx * k][j + dy * k] == w[k] for k in range(L)):
                    for k in range(L):
                        crossed[i + dx * k][j + dy * k] = True
ans = [grid[i][j] for i in range(N) for j in range(N) if not crossed[i][j]]
print(*ans, sep='')