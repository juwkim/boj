g = lambda: tuple(map(int, input().split()))

N, T = g()
time = [0] * 1001
for _ in range(N):
    for _ in range(int(input())):
        s, e = g()
        for i in range(s + 1, e + 1):
            time[i] += 1
for i in range(2, 1001):
    time[i] += time[i-1]

ans = max(range(1001 - T), key=lambda x: (time[x+T] - time[x], -x))
print(ans, ans + T)