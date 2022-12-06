g = lambda: [*map(int, input().split())]

N, L = g()
time = 0
cur = 0
for _ in range(N):
    D, R, G = g()

    time += D - cur
    time += max(0, R - time % (R + G))
    cur = D
    
time += L - cur
print(time)