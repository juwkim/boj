g = lambda: [*map(int, input().split())]

N, T = g()
Min = 1e9
for _ in range(N):
    S, I, C = g()
    if T <= S:
        Min = min(Min, S)
    elif T <= S + I * (C - 1):
        time = S + (T - S + I - 1) // I * I
        Min = min(Min, time)

if Min == 1e9:
    ans = -1
else:
    ans = Min - T
print(ans)