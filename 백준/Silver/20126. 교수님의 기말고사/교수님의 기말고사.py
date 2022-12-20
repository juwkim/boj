g = lambda: [*map(int, input().split())]

ans = -1
N, M, S = g()
time = [[0, 0]] + [g() for _ in range(N)] + [[S, 0]]
time.sort()
for i in range(N + 1):
    if time[i + 1][0] - sum(time[i]) >= M:
        ans = sum(time[i])
        break
print(ans)