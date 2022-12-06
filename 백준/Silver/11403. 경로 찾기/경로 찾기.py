g = lambda: [*map(int, input().split())]

N = int(input())
d = [g() for _ in range(N)]

for i in range(N):
    for s in range(N):
        for e in range(N):
            if d[s][i] + d[i][e] == 2:
                d[s][e] = 1
for line in d:
    print(*line)