g = lambda: map(int, input().split())

N, M = g()
time, money = [0] * N, [0] * N
for _ in range(M):
    t, v, *z = g()
    idx = [i for i in range(N) if time[i] <= t]
    if idx:
        i = min(idx, key=lambda i: z[i])
        time[i] = t + z[i]
        money[i] += v
print(*money)