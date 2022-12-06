g = lambda: [*map(int, input().split())]

N, M = g()
Map = [input() for _ in range(N)]
for size in range(min(N, M), 0, -1):
    if any(Map[i][j] == Map[i+size-1][j] == Map[i][j+size-1] == Map[i+size-1][j+size-1] for i in range(N-size+1) for j in range(M-size+1)):
        print(size * size)
        break