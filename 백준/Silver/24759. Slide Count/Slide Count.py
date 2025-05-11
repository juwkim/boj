N, C, *w = map(int, open(0).read().split())
px = [0] * (N + 1)
s, e = 0, -1
total = 0
while s < N:
    if e == N - 1 or total + w[e + 1] > C:
        total -= w[s]
        s += 1
    else:
        e += 1
        total += w[e]
    px[s] += 1
    px[e + 1] -= 1
for i in range(N):
    px[i + 1] += px[i]
print(*px[:-1])