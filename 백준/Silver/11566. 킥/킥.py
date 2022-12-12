g = lambda: [*map(int, input().split())]

N = int(input())
reality = g()
M = int(input())
dream = g()

Min, Max = 1e9, -1
for i in range(M - N + 1):
    if dream[i] != reality[0]:
        continue
    j = 1
    while i + j * (N - 1) < M:
        if dream[i:i + j * N:j] == reality:
            Min = min(Min, j)
            Max = max(Max, j)
        j += 1
if Max == -1:
    print(-1)
else:
    print(Min - 1, Max - 1)