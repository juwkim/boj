Day = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4}
T, N = map(int, input().split())
for _ in [0] * N:
    D1, H1, D2, H2 = input().split()
    H1, H2 = map(int, [H1, H2])
    T -= H2 - H1 + 24 * (Day[D2] - Day[D1])
print(-1 if T > 48 else 0 if T <= 0 else T)