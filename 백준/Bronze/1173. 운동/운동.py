N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
else:
    time, pulse = 0, m
    while N:
        time += 1
        if pulse + T > M:
            pulse = max(pulse - R, m)
        else:
            pulse += T
            N -= 1
    print(time)