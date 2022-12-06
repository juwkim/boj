g = lambda: map(sum, zip(*[[*map(lambda x: int(x)*2**i, input().split())] for i in range(3, -1, -1)]))
time = [*map(sum, zip(g(), g()))]

for i in range(-1, -6, -1):
    if time[i] > [5, 9][i%2]:
        time[i] -= 6 + i%2 * 4
        time[i-1] += 1

if (h:= time[0] * 10 + time[1]) > 23:
    h = str(h-24).zfill(2)
    time[0], time[1] = map(int, [h[0], h[1]])

for i in range(3, -1, -1):
    print(*map(lambda x: x//2**i, time))
    time = [*map(lambda x: x%2**i, time)]